cmake_minimum_required(VERSION 2.8.3)
project(turtle_control)

## Catkin 패키지를 만드는 방법은 이곳을 참고
## http://wiki.ros.org/catkin/CMakeLists.txt

## To load this project in QtCreator
set(CMAKE_PREFIX_PATH /opt/ros/kinetic)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11 -O2)

## geometry_msgs 등을 바로 찾지 않고 catkin의 COMPONENT로 찾는 이유?
## http://wiki.ros.org/catkin/CMakeLists.txt#Why_Are_Catkin_Packages_Specified_as_Components.3F
## geometry_msgs_INCLUDE_DIRS, nodelet_LIBRARIES 등의 변수를 따로 만들지 않고
## catkin_INCLUDE_DIRS, catkin_LIBRARIES에 모든 패키지 경로를 추가할 수 있기 때문
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  std_msgs
  turtlesim
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

################################################
## Declare ROS messages, services and actions ##
################################################
message("No new ROS message is declared")

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################
message("No dyanamic reconfigure parameters are used")

###################################
## catkin specific configuration ##
###################################
## catkin_package()는 설치와 배포에 필요한 정보를 주는 매크로,
## 	 cmake 파일이나 pkg-config 파일에 반영됨
## INCLUDE_DIRS, LIBRARIES: 다른 패키지에서 
## 	 find_package(catkin REQUIRED COMPONENTS turtle_control) 했을때
## 	 catkin_INCLUDE_DIRS, catkin_LIBRARIES 에 추가될 경로, 파일
## CATKIN_DEPENDS, DEPENDS: 의존하는 catkin 패키지와 시스템 패키지
catkin_package(
  # INCLUDE_DIRS include
  # LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS geometry_msgs std_msgs roscpp turtlesim
  # DEPENDS no system package dependency yet
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

## Specify dependent library files

## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
add_executable(${PROJECT_NAME}_pub src/turtle_control_pub.cpp)
target_link_libraries(${PROJECT_NAME}_pub ${catkin_LIBRARIES})

add_executable(${PROJECT_NAME}_sub src/turtle_control_sub.cpp)
target_link_libraries(${PROJECT_NAME}_sub ${catkin_LIBRARIES})

## Rename C++ executable without prefix
## The above recommended prefix causes long target names, the following renames the
## target back to the shorter version for ease of user use
## e.g. "rosrun someones_pkg node" instead of "rosrun someones_pkg someones_pkg_node"
set_target_properties(${PROJECT_NAME}_pub PROPERTIES OUTPUT_NAME publisher PREFIX "")
set_target_properties(${PROJECT_NAME}_sub PROPERTIES OUTPUT_NAME subscriber PREFIX "")

#############
## Install ##
#############
message("No need to install package")

