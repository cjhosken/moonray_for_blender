#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

set(OCIO_ROOT "$ENV{HOME}/.mfb/dependencies/bl_deps/opencolorio")

# Import target "OpenColorIO::OpenColorIO" for configuration "Release"
set_property(TARGET OpenColorIO::OpenColorIO APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenColorIO::OpenColorIO PROPERTIES
  IMPORTED_LOCATION_RELEASE "${OCIO_ROOT}/lib/libOpenColorIO.so.2.3.2"
  IMPORTED_SONAME_RELEASE "libOpenColorIO.so.2.3"
  )

list(APPEND _cmake_import_check_targets OpenColorIO::OpenColorIO )
list(APPEND _cmake_import_check_files_for_OpenColorIO::OpenColorIO "${OCIO_ROOT}/lib/libOpenColorIO.so.2.3.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
