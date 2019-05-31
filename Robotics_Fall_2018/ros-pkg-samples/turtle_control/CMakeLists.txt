cmake_minimum_required(VERSION 2.8.3)
project(turtle_control)

## To work in qtcreator, append this line before find_package()
set(CMAKE_PREFIX_PATH /opt/ros/kinetic)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11 -O2)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
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
# after catkin_make, there will be the executable target in catkin_ws/devel/lib/${PROJECT_NAME}
# by setting LIBRARIES ${PROJECT_NAME}
catkin_package(
  # INCLUDE_DIRS no header files yet
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS geometry_msgs std_msgs roscpp turtlesim
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

