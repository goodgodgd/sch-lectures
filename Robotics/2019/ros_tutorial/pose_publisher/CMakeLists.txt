cmake_minimum_required(VERSION 2.8.3)
project(pose_publisher)
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  std_msgs
  tf
)
catkin_package(
  CATKIN_DEPENDS geometry_msgs std_msgs tf
)
