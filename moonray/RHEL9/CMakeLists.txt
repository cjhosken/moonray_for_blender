# Copyright 2023-2024 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

# These ExternalProject targets can be used to download, build and
# install many of the Moonray dependencies.
# The targets are chained using dependencies so that they run
# serially.

cmake_minimum_required (VERSION 3.23.1)
project(openmoonray_third_party)

include(ExternalProject)

set(THIS_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(InstallRoot /usr/local CACHE FILEPATH "Install root for dependencies")

ExternalProject_Add(JsonCpp
    URL https://github.com/open-source-parsers/jsoncpp/archive/refs/tags/1.9.5.tar.gz # 1.9.5
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DBUILD_SHARED_LIBS=ON
        -DPYTHON_EXECUTABLE=/usr/bin/python3
        -DJSONCPP_LIB_BUILD_SHARED:BOOL=ON
)
set(CHAIN JsonCpp)

ExternalProject_Add(OpenSubdiv
    URL https://github.com/PixarAnimationStudios/OpenSubdiv/archive/refs/tags/v3_6_0.tar.gz # v3_6_0
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
      -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
      -DCMAKE_BUILD_TYPE=Release
      -DPYTHON_EXECUTABLE=/usr/bin/python3
      -DNO_PTEX=1 -DNO_OMP=1 -DNO_TBB=1 -DNO_CUDA=1 -DNO_GLFW_X11=1 -DNO_DOC=1
      -DNO_OPENCL=1 -DNO_CLEW=1 -DNO_REGRESSION=1 -DNO_EXAMPLES=1 -DNO_TUTORIALS=1 -DNO_GLTESTS=1 
      -DNO_MACOS_FRAMEWORK=1 -DNO_METAL=1 -DNO_TESTS=1 
    DEPENDS ${CHAIN}
)
set(CHAIN OpenSubdiv)

ExternalProject_Add(OpenEXR
    URL https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v3.2.4.tar.gz # v3.2.4
    PATCH_COMMAND patch IlmBase/Half/CMakeLists.txt ${THIS_DIR}/../Imath_include_paths.patch
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DBUILD_SHARED_LIBS=OFF
    DEPENDS ${CHAIN}
)
set(CHAIN OpenEXR)

ExternalProject_Add(Random123
    URL https://github.com/DEShawResearch/random123/archive/refs/tags/v1.14.0.tar.gz # v1.14.0
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND make install-include prefix=${InstallRoot}
    DEPENDS ${CHAIN}
)
set(CHAIN Random123)

ExternalProject_Add(ISPC
    URL https://github.com/ispc/ispc/releases/download/v1.24.0/ispc-v1.24.0-linux.tar.gz
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND cp bin/ispc ${InstallRoot}/bin
    DEPENDS ${CHAIN}
)
set(CHAIN ISPC)

ExternalProject_Add(embree
    URL https://github.com/RenderKit/embree/archive/refs/tags/v4.3.1.tar.gz # v4.3.1
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DEMBREE_ISPC_EXECUTABLE=<INSTALL_DIR>/bin/ispc
        -DEMBREE_ISPC_SUPPORT=ON
        -DEMBREE_IGNORE_INVALID_RAYS=ON
        -DEMBREE_RAY_MASK=ON
        -DEMBREE_MAX_ISA=AVX512
        -DEMBREE_TUTORIALS=OFF
        -DBUILD_SHARED_LIBS=ON
    DEPENDS ${CHAIN}
)
set(CHAIN embree)

ExternalProject_Add(OpenColorIO
    URL https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/refs/tags/v2.3.2.tar.gz # v2.3.2
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DBUILD_SHARED_LIBS=ON
        -DOCIO_BUILD_STATIC=OFF
        -DOCIO_INSTALL_EXT_PACKAGES=ALL
        -DCMAKE_CXX_STANDARD=17
    DEPENDS ${CHAIN}
)
set(CHAIN OpenColorIO)

ExternalProject_Add(OpenImageIO
    URL https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/refs/tags/v2.4.17.0.tar.gz # 2.4.17.0 (not 2.5.12.0 as not supported for EPEL 9)
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DOpenEXR_ROOT=<INSTALL_DIR>
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DUSE_QT=OFF
        -DUSE_PYTHON=OFF
    DEPENDS ${CHAIN}
)
set(CHAIN OpenImageIO)

ExternalProject_Add(OpenImageDenoise
    URL https://github.com/OpenImageDenoise/oidn/releases/download/v2.0.1/oidn-2.0.1.src.tar.gz
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR>
        -DISPC_EXECUTABLE=<INSTALL_DIR>/bin/ispc
        -DTBB_ROOT=<INSTALL_DIR>
        -DOIDN_APPS=OFF
    DEPENDS ${CHAIN}
)
set(CHAIN OpenImageDenoise)

ExternalProject_Add(USD
    URL https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v22.11.tar.gz # v24.05
    INSTALL_DIR ${InstallRoot}
    CMAKE_ARGS
        -DCMAKE_PREFIX_PATH=<INSTALL_DIR>
        -DPXR_ENABLE_PYTHON_SUPPORT=ON
        -DPXR_USE_PYTHON_3=ON
        -DPYTHON_LIBRARIES=/usr/lib64
        -DPYTHON_INCLUDE_DIRS=/usr/include
        -DBoost_LIBRARY_DIR=/usr/lib64
        -DBoost_INCLUDE_DIR=/usr/include
        -DTBB_USE_DEBUG_BUILD=OFF
        -DTBB_ROOT_DIR=/usr
        -DTBB_LIBRARIES=/usr/lib64
        -DTBB_INCLUDE_DIRS=/usr/include ..
        -DPXR_BUILD_TESTS=OFF
        -DPXR_BUILD_EXAMPLES=OFF
        -DPXR_BUILD_TUTORIALS=OFF
        -DPXR_BUILD_USD_TOOLS=OFF
        -DPXR_ENABLE_PTEX_SUPPORT=OFF
        -DPXR_ENABLE_OPENVDB_SUPPORT=OFF
        -DPXR_BUILD_USDVIEW=OFF
        -DBoost_NO_BOOST_CMAKE=ON
        -DBoost_NO_SYSTEM_PATHS=ON
        -DTBB_SUPPRESS_DEPRECATED_MESSAGES=1
    DEPENDS ${CHAIN}
)
set(CHAIN USD)