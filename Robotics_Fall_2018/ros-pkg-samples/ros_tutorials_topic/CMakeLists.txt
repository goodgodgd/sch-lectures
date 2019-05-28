# cmake 최소 버전: ubuntu 16.04에 설치되는 현재 버전은 3.5.1 이므로 만족
cmake_minimum_required(VERSION 2.8.3)
# 반드시!! pakages.xml의 <name>과 같은 이름으로 지정해야 함
project(ros_tutorials_topic)

# 의존성 패키지로 message_generation std_msgs roscpp 들이 필요하며 
# 이 패키지들이 존재하지 않으면 빌드되지 않음
find_package(catkin REQUIRED COMPONENTS message_generation std_msgs roscpp)

# 메시지 선언: 새로 만들 메시지 파일 지정 - MsgTutorial.msg
add_message_files(FILES MsgTutorial.msg)
# 새로 만들 메시지가 의존하는 메시지 지정 - std_msgs
generate_messages(DEPENDENCIES std_msgs)

# 캐킨 패키지 옵션: 라이브러리, 캐킨 의존 패키지(ros 내부의 의존 패키지), 
#					시스템 의존 패키지 (ubuntu에 설치된 패키지) 기술
catkin_package(
  LIBRARIES ros_tutorials_topic
  CATKIN_DEPENDS std_msgs roscpp
)

# 인클루드 디렉토리 설정
# catkin_INCLUDE_DIRS: (캐킨이 관리하는) 설치된 ROS 패키지들의 헤더들이 있는 경로
# 패키지 내부에 헤더 파일이 있다면 ~/catkin_ws/src/package_name/include에 저장한 후
# include_directories(${catkin_INCLUDE_DIRS} include) 이렇게 경로 추가하면 됨
include_directories(${catkin_INCLUDE_DIRS})

# 이 패키지에는 topic_publisher, topic_subscriber 두 개의 실행 파일이 있다.

# topic_publisher 노드에 대한 빌드 옵션
# 실행파일은 src/topic_publisher.cpp 파일로부터 만든다.
add_executable(topic_publisher src/topic_publisher.cpp)
# 실행파일을 빌드하기 전에 메시지 파일 등을 먼저 헤더로 변환하여 빌드해야 한다.
# 새로운 메시지를 정의할 때 관습적으로 붙이자.
add_dependencies(topic_publisher ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
# cmake 명령중 link_libraries 는 전체 빌드시 필요한 라이브러리를 지정한다.
# target_link_libraries 는 특정 타겟을 빌드할 때 필요한 라이브러리를 지정한다.
# 참조: https://www.tuwlab.com/27260
target_link_libraries(topic_publisher ${catkin_LIBRARIES})

# topic_subscriber 노드에 대한 빌드 옵션 (topic_publisher와 동일)
add_executable(topic_subscriber src/topic_subscriber.cpp)
add_dependencies(topic_subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(topic_subscriber ${catkin_LIBRARIES})

