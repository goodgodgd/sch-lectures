cmake_minimum_required(VERSION 2.8.3)
project(image_topic_py3)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  std_msgs
)
catkin_package(
   CATKIN_DEPENDS rospy sensor_msgs std_msgs
)
