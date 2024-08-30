# - Configuration file for the pxr project
# Defines the following variables:
# PXR_MAJOR_VERSION - Major version number.
# PXR_MINOR_VERSION - Minor version number.
# PXR_PATCH_VERSION - Patch version number.
# PXR_VERSION       - Complete pxr version string.
# PXR_INCLUDE_DIRS  - Root include directory for the installed project.
# PXR_LIBRARIES     - List of all libraries, by target name.
# PXR_foo_LIBRARY   - Absolute path to individual libraries.
# The preprocessor definition PXR_STATIC will be defined if appropriate

get_filename_component(PXR_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)

set(PXR_MAJOR_VERSION "0")
set(PXR_MINOR_VERSION "23")
set(PXR_PATCH_VERSION "11")
set(PXR_VERSION "2311")


# Set the root directory for USD
set(USD_ROOT "$ENV{HOME}/.mfb/dependencies/bl_deps/usd")
# Path to the USD monolithic library
set(PXR_usd_ms_LIBRARY "${USD_ROOT}/lib/libusd_ms.so")

# Set include directories
set(PXR_INCLUDE_DIRS "${USD_ROOT}/include" CACHE PATH "Path to the pxr include directory")

# Initialize PXR_LIBRARIES with the path to the monolithic library
set(PXR_LIBRARIES "${PXR_usd_ms_LIBRARY}")

# If PXR_STATIC is defined, include Windows-specific libraries
if(NOT ON)
    if(WIN32)
        list(APPEND PXR_LIBRARIES Shlwapi.lib)
        list(APPEND PXR_LIBRARIES Dbghelp.lib)
    endif()
    add_definitions(-DPXR_STATIC)
endif()

# Provide useful information for debugging
message(STATUS "PXR_INCLUDE_DIRS: ${PXR_INCLUDE_DIRS}")
message(STATUS "PXR_LIBRARIES: ${PXR_LIBRARIES}")

include_directories(${PXR_INCLUDE_DIRS})
link_libraries(${PXR_LIBRARIES})

set(BL_PYTHON_ROOT "$ENV{HOME}/.mfb/dependencies/bl_deps/python")

set(PYTHON_INCLUDE_DIRS "${BL_PYTHON_ROOT}/include/python3.11")
set(PYTHON_LIBRARIES "${BL_PYTHON_ROOT}/lib/libpython3.11.a")

message(STATUS "PYTHON_INCLUDE_DIRS:" ${PYTHON_INCLUDE_DIRS})
message(STATUS "PYTHON_LIBRARIES:" ${PYTHON_LIBRARIES})
include_directories(${PYTHON_INCLUDE_DIRS})
link_libraries(${PYTHON_LIBRARIES})

# Find and configure Boost
find_package(Boost 1.82 REQUIRED COMPONENTS python311 iostreams regex)



if (Boost_FOUND)
    # Set to use static Boost libraries
    set(Boost_USE_STATIC_LIBS ON)
    set(Boost_USE_MULTITHREADED ON)
    set(Boost_USE_STATIC_RUNTIME OFF)

    set(Boost_LIBRARIES "$ENV{HOME}/.mfb/dependencies/bl_deps/boost/lib")
    set(Boost_INCLUDE_DIRS "$ENV{HOME}/.mfb/dependencies/bl_deps/boost/include")

    message(STATUS "Boost_INCLUDE_DIRS: ${Boost_INCLUDE_DIRS}")
    message(STATUS "Boost_LIBRARIES: ${Boost_LIBRARIES}")

    include_directories(${Boost_INCLUDE_DIRS})
    link_directories(${Boost_LIBRARIES})
else()
    message(FATAL_ERROR "Could not find Boost libraries.")
endif()
