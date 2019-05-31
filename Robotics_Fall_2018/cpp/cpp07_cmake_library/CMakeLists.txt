cmake_minimum_required(VERSION 3.0)
project("myqt5" VERSION 1.1)

set(CMAKE_CXX_COMPILER g++)
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_INSTALL_PREFIX ${CMAKE_CURRENT_SOURCE_DIR}/devel)
message("=== install prefix ${CMAKE_INSTALL_PREFIX}")
add_compile_options(-Wall -std=c++14 -O2 -fPIC)

set(CMAKE_PREFIX_PATH /opt/Qt5.12.3/5.12.3/gcc_64)
find_package(Qt5Core REQUIRED)
message("=== find package(Qt5Core) generated Qt5Core_DIR=${Qt5Core_DIR}, Qt5Core_CONFIG=${Qt5Core_CONFIG}")
message("=== find package(Qt5Core) loaded Qt5Core_INCLUDE_DIRS=${Qt5Core_INCLUDE_DIRS}")
include_directories(${Qt5Core_INCLUDE_DIRS})
# include_directories("${Qt5Core_DIR}/../../../include")
# include_directories("/opt/Qt5.12.3/5.12.3/gcc_64/include")
link_directories("${Qt5Core_DIR}/../..")
# link_directories(/opt/Qt5.12.3/5.12.3/gcc_64/lib)
link_libraries(Qt5Core)

set(OUTPUT_SHARED_LIB "${CMAKE_PROJECT_NAME}")
set(OUTPUT_STATIC_LIB "${CMAKE_PROJECT_NAME}_stat")

add_library(${OUTPUT_SHARED_LIB} SHARED myqt5.cpp)
add_library(${OUTPUT_STATIC_LIB} STATIC myqt5.cpp)
set_target_properties(${OUTPUT_SHARED_LIB} PROPERTIES VERSION ${PROJECT_VERSION} PUBLIC_HEADER myqt5.h)
set_target_properties(${OUTPUT_STATIC_LIB} PROPERTIES VERSION ${PROJECT_VERSION} PUBLIC_HEADER myqt5.h)

set(OUTPUT_EXEC "${CMAKE_PROJECT_NAME}_app")
add_executable(${OUTPUT_EXEC} main.cpp)
target_link_libraries(${OUTPUT_EXEC} ${OUTPUT_SHARED_LIB})

install(TARGETS ${OUTPUT_SHARED_LIB} ${OUTPUT_STATIC_LIB} ${OUTPUT_EXEC}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        PUBLIC_HEADER DESTINATION include
        )

