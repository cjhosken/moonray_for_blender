#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "$0")")"

mkdir "$HOME/.dreamworks"
cd "$HOME/.dreamworks"

git clone --recurse-submodules https://github.com/dreamworksanimation/openmoonray.git ./source

rm -rf ./dependencies
mkdir ./dependencies

sudo -s source ./source/building/Rocky9/install_packages.sh
cp -r /installs/* ./dependencies
sudo rm -rf /installs

export PATH=$HOME/.dreamworks/dependencies/cmake-3.23.1-linux-x86_64/bin:/usr/local/cuda/bin:${PATH}

cd ./dependencies
cp $SCRIPT_DIR/optix.sh ./optix.sh
bash ./optix.sh --skip-license --exclude-subdir
cd ..

rm -rf ./build
mkdir ./build
cd ./build

cmake ../source/building/Rocky9 -DInstallRoot="$HOME/.dreamworks/dependencies"
cmake --build . -- -j $(nproc)

rm -rf *
cmake ../source -DPYTHON_EXECUTABLE=python3 -DBOOST_PYTHON_COMPONENT_NAME=python39 -DABI_VERSION=0 -DCMAKE_PREFIX_PATH="$HOME/.dreamworks/dependencies"
cmake --build . -j $(nproc)

rm -rf ../installs
mkdir ../installs
mkdir ../installs/openmoonray
cmake --install . --prefix ../installs/openmoonray

source ../installs/openmoonray/scripts/setup.sh