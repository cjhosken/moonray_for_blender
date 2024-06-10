#!/bin/bash

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}


OS_DIST="RHEL9"

# Function to update package manager and install required dependencies
update_and_install() {
  local package_manager=$1

  case $package_manager in
    apt-get)
      $package_manager update
      $package_manager install -y git cmake build-essential libtbb-dev
      ;;
    yum)
      $package_manager update -y
      $package_manager install -y git cmake gcc-c++ make tbb-devel
      ;;
    *)
      echo "Unsupported package manager: $package_manager"
      exit 1
      ;;
  esac
}

# Check which package manager is available
if command_exists apt-get; then
  echo "Detected Ubuntu/Debian-based system"
  update_and_install "apt-get"
elif command_exists yum; then
  echo "Detected Red Hat/CentOS-based system"
  update_and_install "yum"
else
  echo "Unable to determine the package manager. Please install the required dependencies manually."
  exit 1
fi

# Get the non-sudo user's home directory
non_sudo_home_dir=$(eval echo "~$SUDO_USER")
script_dir=/home/cjhosken/Documents/programming/moonray_for_blender

# Define the installation directory
INSTALL_DIR=$non_sudo_home_dir/dreamworks
SOURCE_DIR=$INSTALL_DIR/source
MOONRAY_DIR=$INSTALL_DIR/moonray

BUILD_DIR=$INSTALL_DIR/build


if [ ! -d "$SOURCE_DIR" ]; then
  mkdir -p "$INSTALL_DIR"
  chown -R "$SUDO_USER:$SUDO_USER" "$INSTALL_DIR"
  chmod -R 755 "$INSTALL_DIR"
fi

if [ -d "$SOURCE_DIR" ]; then
    read -p "Source directory already exists. Do you want to override it? (y/n): " answer
    case ${answer,,} in
        y)
            rm -rf "$SOURCE_DIR"
            git clone --recurse-submodules https://github.com/dreamworksanimation/openmoonray.git "$SOURCE_DIR"
            ;;
        n)
            echo "Continuing with current source..."
          
            ;;
        *)
            echo "Invalid input. Exiting..."
            exit 1
            ;;
    esac
else
git clone --recurse-submodules https://github.com/dreamworksanimation/openmoonray.git "$SOURCE_DIR"
fi

# Change ownership and permissions
chown -R "$SUDO_USER:$SUDO_USER" "$SOURCE_DIR"
chmod -R 755 "$SOURCE_DIR"

if [ ! -d "$BUILD_DIR" ]; then
mkdir -p "$BUILD_DIR"
fi
chown -R "$SUDO_USER:$SUDO_USER" "$BUILD_DIR"
chmod -R 755 "$BUILD_DIR"


cd "$BUILD_DIR"

if [ -d "$INSTALL_DIR/source/building/$OS_DIST" ]; then
rm -rf "$INSTALL_DIR/source/building/$OS_DIST"
fi

cp -r "$script_dir/moonray/$OS_DIST/" "$INSTALL_DIR/source/building/$OS_DIST/"
chown -R "$SUDO_USER:$SUDO_USER" "$INSTALL_DIR/source/building/$OS_DIST"
chmod -R 755 "$INSTALL_DIR/source/building/$OS_DIST"

if [ -d "/installs" ]; then
rm -rf "/installs"
fi

mkdir -p /installs

cd "$BUILD_DIR"

source "$SOURCE_DIR/building/$OS_DIST/install_packages.sh"

echo "Using Cmake Version"
cmake --version

echo "Building Dependencies..."

cmake "$SOURCE_DIR/building/$OS_DIST/"
cmake --build . -- -j $(nproc)

chown -R "$SUDO_USER:$SUDO_USER" "$BUILD_DIR"
chmod -R 755 "$BUILD_DIR"

echo "Dependencies Built!"


echo "Loading Optix Headers"

if [ ! -f "/usr/local/include/optix.h" ]; then
cd "/usr/local/"
bash "$SOURCE_DIR/building/$OS_DIST/install_optix.sh" --skip-license
fi

echo "Optix Headers Loaded!"

echo "Building MoonRay..."

cd "$BUILD_DIR"


#-DBUILD_QT_APPS=NO
#-DMOONRAY_USE_CUDA=NO
cmake "$SOURCE_DIR" -DPYTHON_EXECUTABLE=python3 -DBOOST_PYTHON_COMPONENT_NAME=python39 -DABI_VERSION=0

cmake --build . -- -j $(nproc)

echo "MoonRay Built!"

echo "Installing Moonray..."

if [ ! -d "$MOONRAY_DIR" ]; then
mkdir "$MOONRAY_DIR"
fi

cd "$BUILD_DIR"

cmake --install . --prefix "$MOONRAY_DIR"

# Set ownership and permissions for installed files
chown -R "$SUDO_USER:$SUDO_USER" "$MOONRAY_DIR"
chmod -R 755 "$MOONRAY_DIR"

echo "MoonRay installation completed successfully!"

echo "Running Test"

source "$MOONRAY_DIR/scripts/setup.sh"
moonray -in $SOURCE_DIR/testdata/rectangle.rdla -out /tmp/rectangle.exr
