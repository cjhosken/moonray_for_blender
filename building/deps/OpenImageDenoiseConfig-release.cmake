#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

set(OIDN_ROOT "$ENV{HOME}/.mfb/dependencies/bl_deps/openimagedenoise")

# Import target "OpenImageDenoise_core" for configuration "Release"
set_property(TARGET OpenImageDenoise_core APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenImageDenoise_core PROPERTIES
  IMPORTED_LOCATION_RELEASE "${OIDN_ROOT}/lib/libOpenImageDenoise_core.so.2.2.2"
  IMPORTED_SONAME_RELEASE "libOpenImageDenoise_core.so.2.2.2"
  )

list(APPEND _cmake_import_check_targets OpenImageDenoise_core )
list(APPEND _cmake_import_check_files_for_OpenImageDenoise_core "${OIDN_ROOT}/lib/libOpenImageDenoise_core.so.2.2.2" )

# Import target "OpenImageDenoise" for configuration "Release"
set_property(TARGET OpenImageDenoise APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenImageDenoise PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "OpenImageDenoise_core"
  IMPORTED_LOCATION_RELEASE "${OIDN_ROOT}/lib/libOpenImageDenoise.so.2.2.2"
  IMPORTED_SONAME_RELEASE "libOpenImageDenoise.so.2"
  )

list(APPEND _cmake_import_check_targets OpenImageDenoise )
list(APPEND _cmake_import_check_files_for_OpenImageDenoise "${OIDN_ROOT}/lib/libOpenImageDenoise.so.2.2.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
