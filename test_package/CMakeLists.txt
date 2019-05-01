cmake_minimum_required(VERSION 2.8.12)
project(test_package)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

#========================================
#	find zlib
#========================================
SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_BINARY_DIR})
FIND_PACKAGE("zlib")

IF(NOT ${zlib_FOUND})
    MESSAGE(FATAL_ERROR "Can't find zlib")
ENDIF()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS} zlib::zlib)
