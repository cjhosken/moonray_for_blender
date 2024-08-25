#!/bin/bash

sudo -v
while true; do sudo -n true; sleep 60; done 2>/dev/null &

SCRIPT_DIR="$(dirname "$(realpath "$0")")"

MFB_DIR="$HOME/.mfb"

mkdir -p "$MFB_DIR"
cd "$MFB_DIR"

git clone --recurse-submodules https://github.com/dreamworksanimation/openmoonray.git $MFB_DIR/source

sudo rm -rf $MFB_DIR/dependencies
mkdir $MFB_DIR/dependencies

rm -rf $MFB_DIR/source/building/RHEL9
cp -r $SCRIPT_DIR/RHEL9 $MFB_DIR/source/building/RHEL9

sudo -s source $MFB_DIR/source/building/RHEL9/install_packages.sh

rm -rf $MFB_DIR/build
mkdir $MFB_DIR/build
cd $MFB_DIR/build

cmake $MFB_DIR/source/building/RHEL9 -DInstallRoot="$MFB_DIR/dependencies"
sudo -s cmake --build . -- -j $(nproc)

cd $MFB_DIR/dependencies
cp $SCRIPT_DIR/linux_optix.sh $MFB_DIR/dependencies/linux_optix.sh
sudo bash $MFB_DIR/dependencies/linux_optix.sh --skip-license --exclude-subdir

sudo rm -rf $MFB_DIR/build/*
cd $MFB_DIR/builds


BLENDER_DIR="$HOME/"

cmake $MFB_DIR/source \
  -DPYTHON_EXECUTABLE="$HOME/programming/blender-git/blender/lib/linux_x64/python/" \
  -DABI_VERSION=0 \
  -DCMAKE_PREFIX_PATH="$MFB_DIR/dependencies" \
  -DPXR_INCLUDE_DIRS="$HOME/programming/blender-git/blender/lib/linux_x64/usd/include" \
  -DPXR_LIBRARY_DIRS="$HOME/programming/blender-git/blender/lib/linux_x64/usd/lib/usd" \
  -DPYTHON_INCLUDE_DIRS="$HOME/programming/blender-git/blender/lib/linux_x64/python/include" \
  -DPYTHON_LIBRARY=/usr/lib64/libpython3.9.so

cmake --build . -j $(nproc)

rm -rf $MFB_DIR/installs
mkdir $MFB_DIR/installs
mkdir $MFB_DIR/installs/openmoonray
cmake --install . --prefix $MFB_DIR/installs/openmoonray

source $MFB_DIR/installs/openmoonray/scripts/setup.sh

SOURCE_LINE="source $MFB_DIR/installs/openmoonray/scripts/setup.sh"

# The .bashrc file path
BASHRC_PATH="$HOME/.bashrc"

# Check if the line already exists in .bashrc
if grep -Fxq "$SOURCE_LINE" "$BASHRC_PATH"; then
    echo "The line already exists in .bashrc."
else
    # Ensure the file ends with a newline before adding the new line
    echo >> "$BASHRC_PATH"

    # Add the source line to .bashrc
    echo "$SOURCE_LINE" >> "$BASHRC_PATH"
    echo "The line has been added to .bashrc."
fi


cd $SCRIPT_DIR

kill $!