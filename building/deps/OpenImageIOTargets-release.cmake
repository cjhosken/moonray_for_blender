#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

set(OIIO_ROOT "$ENV{HOME}/.mfb/dependencies/bl_deps/openimageio")

# Import target "OpenImageIO::OpenImageIO_Util" for configuration "Release"
set_property(TARGET OpenImageIO::OpenImageIO_Util APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenImageIO::OpenImageIO_Util PROPERTIES
  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/lib/libOpenImageIO_Util.so.2.5.6"
  IMPORTED_SONAME_RELEASE "libOpenImageIO_Util.so.2.5"
  )

list(APPEND _cmake_import_check_targets OpenImageIO::OpenImageIO_Util )
list(APPEND _cmake_import_check_files_for_OpenImageIO::OpenImageIO_Util "${OIIO_ROOT}/lib/libOpenImageIO_Util.so.2.5.6" )

# Import target "OpenImageIO::OpenImageIO" for configuration "Release"
set_property(TARGET OpenImageIO::OpenImageIO APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenImageIO::OpenImageIO PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "TBB::tbb;OpenColorIO::OpenColorIO"
  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/lib/libOpenImageIO.so.2.5.6"
  IMPORTED_SONAME_RELEASE "libOpenImageIO.so.2.5"
  )

list(APPEND _cmake_import_check_targets OpenImageIO::OpenImageIO )
list(APPEND _cmake_import_check_files_for_OpenImageIO::OpenImageIO "${OIIO_ROOT}/lib/libOpenImageIO.so.2.5.6" )

# Import target "OpenImageIO::iconvert" for configuration "Release"
#set_property(TARGET OpenImageIO::iconvert APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
#set_target_properties(OpenImageIO::iconvert PROPERTIES
#  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/bin/iconvert"
#  )

#list(APPEND _cmake_import_check_targets OpenImageIO::iconvert )
#list(APPEND _cmake_import_check_files_for_OpenImageIO::iconvert "${OIIO_ROOT}/bin/iconvert" )

# Import target "OpenImageIO::idiff" for configuration "Release"
set_property(TARGET OpenImageIO::idiff APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenImageIO::idiff PROPERTIES
  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/bin/idiff"
  )

list(APPEND _cmake_import_check_targets OpenImageIO::idiff )
list(APPEND _cmake_import_check_files_for_OpenImageIO::idiff "${OIIO_ROOT}/bin/idiff" )

# Import target "OpenImageIO::igrep" for configuration "Release"
#set_property(TARGET OpenImageIO::igrep APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
#set_target_properties(OpenImageIO::igrep PROPERTIES
#  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/bin/igrep"
#  )

#list(APPEND _cmake_import_check_targets OpenImageIO::igrep )
#list(APPEND _cmake_import_check_files_for_OpenImageIO::igrep "${OIIO_ROOT}/bin/igrep" )

# Import target "OpenImageIO::iinfo" for configuration "Release"
#set_property(TARGET OpenImageIO::iinfo APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
#set_target_properties(OpenImageIO::iinfo PROPERTIES
#  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/bin/iinfo"
#  )

#list(APPEND _cmake_import_check_targets OpenImageIO::iinfo )
#list(APPEND _cmake_import_check_files_for_OpenImageIO::iinfo "${OIIO_ROOT}/bin/iinfo" )

# Import target "OpenImageIO::maketx" for configuration "Release"
set_property(TARGET OpenImageIO::maketx APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenImageIO::maketx PROPERTIES
  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/bin/maketx"
  )

list(APPEND _cmake_import_check_targets OpenImageIO::maketx )
list(APPEND _cmake_import_check_files_for_OpenImageIO::maketx "${OIIO_ROOT}/bin/maketx" )

# Import target "OpenImageIO::oiiotool" for configuration "Release"
set_property(TARGET OpenImageIO::oiiotool APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenImageIO::oiiotool PROPERTIES
  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/bin/oiiotool"
  )

list(APPEND _cmake_import_check_targets OpenImageIO::oiiotool )
list(APPEND _cmake_import_check_files_for_OpenImageIO::oiiotool "${OIIO_ROOT}/bin/oiiotool" )

# Import target "OpenImageIO::iv" for configuration "Release"
#set_property(TARGET OpenImageIO::iv APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
#set_target_properties(OpenImageIO::iv PROPERTIES
#  IMPORTED_LOCATION_RELEASE "${OIIO_ROOT}/bin/iv"
#  )

#list(APPEND _cmake_import_check_targets OpenImageIO::iv )
#list(APPEND _cmake_import_check_files_for_OpenImageIO::iv "${OIIO_ROOT}/bin/iv" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
