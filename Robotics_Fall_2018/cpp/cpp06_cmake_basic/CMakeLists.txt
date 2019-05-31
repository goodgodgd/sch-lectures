cmake_minimum_required(VERSION 3.0)
project("HelloCMake")
message("project name: ${CMAKE_PROJECT_NAME}")
message("install dir: ${CMAKE_INSTALL_PREFIX}")

set(CMAKE_CXX_COMPILER g++)
set(CMAKE_BUILD_TYPE Release)
set(SOURCE_FILES main.cpp foo.cpp bar.cpp)
set(CMAKE_PREFIX_PATH /usr/lib /usr/local/lib)
message("set vars: ${CMAKE_BUILD_TYPE}, ${SOURCE_FILES}")

add_executable(myapp ${SOURCE_FILES})

