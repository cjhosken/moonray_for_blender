#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

set(IMATH_ROOT "$ENV{HOME}/.mfb/dependencies/bl_deps/imath")

# Import target "Imath::Imath" for configuration "Release"
set_property(TARGET Imath::Imath APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(Imath::Imath PROPERTIES
  IMPORTED_LOCATION_RELEASE "${IMATH_ROOT}/lib/libImath.so.30.0.1"
  IMPORTED_SONAME_RELEASE "libImath.so.30"
  )

list(APPEND _cmake_import_check_targets Imath::Imath )
list(APPEND _cmake_import_check_files_for_Imath::Imath "${IMATH_ROOT}/lib/libImath.so.30.0.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
