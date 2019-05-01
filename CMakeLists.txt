cmake_minimum_required(VERSION 2.8.12)
project(cmake_wrapper)
set(CMAKE_CXX_STANDARD 17)

#========================================
#	find zlib
#========================================
SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_BINARY_DIR})
FIND_PACKAGE("zlib")

IF(NOT ${zlib_FOUND})
    MESSAGE(FATAL_ERROR "Can't find zlib")
ENDIF()


message(STATUS "Conan CMake Wrapper")
include(conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory("source_subfolder")
