# cmake 최소 버전: ubuntu 18.04에 설치되는 현재 버전은 3.10.2 이므로 만족
cmake_minimum_required(VERSION 2.8.3)
# package.xml에 지정된 이름과 동일한 프로젝트 이름
project(hello_ros)

# ROS Kinetic 이후로는 C++11을 사용할 수 있다.
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS roscpp std_msgs)
# find_package(Boost REQUIRED COMPONENTS system)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME}_node src/hello_ros_node.cpp)
add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

