# Create ROS package

교재 7.2장에서 ROS에서 토픽을 발행하고 구독하는 예제를 따라하며  
ROS 패키지를 만드는 과정도 함께 공부해 봅시다. 

## 1. 패키지 생성

패키지는 `catkin_create_pkg` 명령어를 이용해 생성할 수 있다.
```bash
# ros 패키지는 ~/catkin_ws/src 이곳에 생성해야 합니다.
$ cd ~/catkin_ws/src
# catkin_create_pkg [패키지 이름] [의존 패키지들]
$ catkin_create_pkg ros_tutorials_topic message_generation std_msgs roscpp
$ ls ros_tutorials_topic
CMakeLists.txt : 빌드 설정 파일
package.xml : 패키지 설정 파일
```

#### make, cmake, and catkin  
- 리눅스의 기본 빌드 시스템은 make이고 make를 이용해 빌드를 하기 위해서는 makefile 이라는 스크립트 필요  
- makefile 은 어떤 소스를 빌드해야 하는지 어떤 라이브러리를 링크해야 하는지 등의 빌드에 필요한 정보를 정해진 문법에 따라 기술함
- 문제는 makefile 이 쉘 스크립트 기반으로 되어 있어서 프로젝트가 복잡해 질수록 읽고 쓰기가 어렵다는 것
- cmake는 이 makefile을 좀 더 쉽게 생성할 수 있게 도와주는 빌드 시스템으로 현재 가장 일반적으로 많이 쓰임
- cmake는 빌드시 생기는 중간 생성물을 (.o) 신경쓰지 않고 소스에서 만들어질 결과물 (실행파일, 라이브러리)만 지정해주면 makefile 을 생성해 줌
- 물론 cmake 자체도 CMakeList.txt 라는 스크립트 파일을 cmake 문법에 따라 작성해줘야만 함
- ~~그럼 이걸 왜하나~~ 그래도 makefile을 직접 작성하는 것 보다는 훨씬 쉬움
- catkin은 cmake를 기반으로 ros를 위한 기능들이 추가된 빌드시스템
- catkin도 똑같이 CMakeList.txt 를 통해 빌드 설정을 하고 문법도 cmake와 동일하나 몇 가지 기능만 추가됨  

---

## 2. 패키지 설정 파일 수정

`catkin_create_pkg` 명령어로 패키지를 생성하면 기본적으로 `CMakeLists.txt`와 `package.xml`이 생기고 주석을 통해 다양한 설정들을 가이드하고 있다.  
- package.xml: ROS에서 패키지를 관리하는데 필요한 정보 기술   
설치 시  필요한 의존 패키지 정보, 패키지를 배포하는데 필요한 저자, 라이센스 등의 정보  
- CMakeLists.txt: 로컬에서 소스를 빌드하는데 필요한 설정 지정  

두 파일에 다양한 설정 항목들이 있는데 모두 다 항상 필요한 것은 아니고 예제에 나오는 설정 위주로 의미와 사용법을 알아보자.  

### 2.1 package.xml

다음은 ros_tutorials_topic을 위해 package.xml 을 작성한 예시이다.
```xml
<?xml version="1.0"?>
<!-- packages.xml: ros에서 패키지를 관리하는데 필요한 정보 담음 -->
<!-- 공식 패키지로 업로드시 공개해야 할 정보들 포함: 저자, 저작권 등 -->
<!-- 의존 패키지들을 지정하면 빌드시 설치되지 않은 의존 패키지 자동 설치 -->
<!-- xml version: 필수는 아님 -->

<package>
  <!-- 패키지 이름은 자동으로 지정됨, 수정할 시 이름이 틀리지 않게 주의 -->
  <name>ros_tutorials_topic</name>
  <!-- 기본 생성시 버전은 0.0.0 인데 원하는대로 수정 가능 -->
  <version>0.1.0</version>

  <!-- 위키를 만들면 자동으로 이 문구가 업로드 됨 -->
  <description>ROS turtorial package to learn the topic</description>
  <!-- 저작권, 저자, 관리자 등 추가정보 -->
  <license>BSD</license>
  <author email="id@sch.ac.kr">your name</author>
  <maintainer email="id@sch.ac.kr">your name</maintainer>
  <url type="repository">https://github.com/goodgodgd/Fall_2018_Lectures</url>
  <!-- 빌드 시스템 지정, catkin 쓰면 됨 -->
  <buildtool_depend>catkin</buildtool_depend>
  <!-- 빌드 할 때 의존성: 언어는 cpp, 표준 메시지 사용, 새 메시지 생성 -->
  <build_depend>roscpp</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_depend>message_generation</build_depend>
  <!-- 실행 할 때 의존성: 언어는 cpp, 표준 메시지 사용, 새 메시지 사용 -->
  <run_depend>roscpp</run_depend>
  <run_depend>std_msgs</run_depend>
  <run_depend>message_runtime</run_depend>
  <export></export>
</package>
```

### 2.2 CMakeList.txt

```cmake
# cmake 최소 버전: ubuntu 16.04에 설치되는 현재 버전은 3.5.1 이므로 만족
cmake_minimum_required(VERSION 2.8.3)
# 반드시!! pakages.xml의 <name>과 같은 이름으로 지정해야 함
project(ros_tutorials_topic)

# 의존성 패키지로 message_generation std_msgs roscpp 들이 필요하며 이 패키지들이 존재하지 않으면 빌드되지 않음
find_package(catkin REQUIRED COMPONENTS message_generation std_msgs roscpp)

# 메시지 선언: 새로 만들 메시지 파일 지정 - MsgTutorial.msg
add_message_files(FILES MsgTutorial.msg)
# 새로 만들 메시지가 의존하는 메시지 지정 - std_msgs
generate_messages(DEPENDENCIES std_msgs)

# 캐킨 패키지 옵션: 라이브러리, 캐킨 의존 패키지(ros 내부의 의존 패키지), 
#	시스템 의존 패키지 (ubuntu에 설치된 패키지) 기술
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

# topic_subscriber 노드에 대한 빌드 옵션
add_executable(topic_subscriber src/topic_subscriber.cpp)
add_dependencies(topic_subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(topic_subscriber ${catkin_LIBRARIES})
```
---

## 3. 메시지 파일 작성

#### 용어 정리
메시지라는 용어는 원래 노드간의 통신(토픽, 서비스, 액션)에 사용되는 일반적인 데이터 형식을 의미한다.  
메시지를 파일로 정의할 때는 토픽의 경우 .msg 파일 (메시지 파일)을 작성하고 서비스는 .srv 파일 (서비스 파일)을 작성해야 한다.  
여기서는 토픽만을 다루고 있기 때문에 용어가 혼용되는데 여기서 말하는 메시지는 주로 **토픽의 데이터 형식(=메시지 파일)**을 말한다.  

노드는 메시지에 고유의 네임을 붙여 정보를 보내고 수신 측에서도 네임으로 메시지를 식별하여 받는다.  
기본 메시지 자료형과 메시지 구성 방법은 위키를 참조한다. http://wiki.ros.org/msg  

`CMakeLists.txt`에서 메시지 파일을 추가하기 위해 다음 줄을 추가하였다.
```cmake
add_message_files(FILES MsgTutorial.msg)
```
메시지 파일을 추가해 보자.
```bash
$ roscd ros_tutorials_topic
$ mkdir msg
$ cd msg
$ gedit MsgTutorial.msg
```
gedit 창에서 다음과 같은 간단한 메시지를 작성해보자. time은 ros의 기본 타입으로서 seconds / nano seconds 두 가지 단위로 시간을 표현하며 int32 정수단위로 시간을 기록한다. time은 C++에서  ros::Time 형식으로 사용된다.
```
time stamp
int32 data
```
---

## 4. 퍼블리셔 노드 작성

퍼블리셔 노드의 실행파일을 생성하기 위해 `CMakeLists.txt`에 다음 줄을 추가하였다. 
```cmake
add_executable(topic_publisher src/topic_publisher.cpp)
```
실행 파일을 `src/topic_publisher.cpp` 로부터 만든다고 했으므로 소스 파일을 만든다.
```bash
$ roscd ros_tutorials_topic/src
$ gedit topic_publisher.cpp
```
소스 파일을 다음과 같이 작성하자.
```cpp
// ROS Default Header File
#include "ros/ros.h"
// MsgTutorial Message Header. 빌드시 MsgTutorial.msg 파일로부터 자동 생성됨
#include "ros_tutorials_topic/MsgTutorial.h"

int main(int argc, char **argv)		// Node Main Function
{
  // 노드 네임 초기화: 특별히 이름을 지정하지 않고 노드를 실행하면 "/topic_publisher" 란 네임을 갖게 된다.
  ros::init(argc, argv, "topic_publisher");
  // Node handle declaration for communication with ROS system
  ros::NodeHandle nh;

  // 퍼블리셔 선언: 'MsgTutorial' 타입의 메시지를 발행하는 객체 'ros_tutorial_pub'를 NodeHandle을 통해 생성
  // 발행 할 토픽 네임: 'ros_tutorial_msg' 
  // 퍼블리셔 큐 사이즈: 100 (100개의 메시지까지 버퍼에 쌓아둘 수 있음)
  ros::Publisher ros_tutorial_pub = 
  	nh.advertise<ros_tutorials_topic::MsgTutorial>
  		("ros_tutorial_msg", 100);

  // loop 빈도 설정, 초당 10번의 loop 반복
  ros::Rate loop_rate(10);

  // Declares message 'msg' in 'MsgTutorial' message file format
  ros_tutorials_topic::MsgTutorial msg;     
  int count = 0;

  // ros나 노드 상태에 이상이 생기지 않는 한 무한 반복
  while (ros::ok())
  {
    // msg.stamp 에 현재 시각 저장, msg.data 에 'count' 저장
    msg.stamp = ros::Time::now();
    msg.data  = count;

	// msg 변수 정보 출력
    ROS_INFO("send msg.stamp.sec = %d", msg.stamp.sec); 
    ROS_INFO("send msg.stamp.nsec = %d", msg.stamp.nsec);
    ROS_INFO("send msg.data = %d", msg.data);

	// msg를 발행
    ros_tutorial_pub.publish(msg);
    
    // 앞서 지정한 주기만큼(0.1s) 정지
    loop_rate.sleep();
    ++count;
  }
  return 0;
}
```
---

## 5. 서브스크라이버 노드 작성

퍼블리셔와 마찬가지로 서브스크라이버 노드의 실행파일을 생성하기 위해 `CMakeLists.txt`에 다음 줄을 추가하였다. 

```cmake
add_executable(topic_subscriber src/topic_subscriber.cpp)
```

실행 파일을 `src/topic_subscriber.cpp` 로부터 만든다고 했으므로 소스 파일을 만든다.

```bash
$ roscd ros_tutorials_topic/src
$ gedit topic_subscriber.cpp
```

소스 파일을 다음과 같이 작성하자.
```cpp
// ROS Default Header File
#include "ros/ros.h"
// MsgTutorial Message Header. 빌드시 MsgTutorial.msg 파일로부터 자동 생성됨
#include "ros_tutorials_topic/MsgTutorial.h"

// 'ros_tutorial_msg'라는 네임을 갖는 메시지가 수신되었을 때 실행되는 함수
// 'ros_tutorials_topic' 패키지의 'MsgTutorial' 메시지를 받도록 되어있다.
void msgCallback(const ros_tutorials_topic::MsgTutorial::ConstPtr& msg)
{
  // 수신된 메시지 데이터 프린트
  ROS_INFO("recieve msg.stamp.sec = %d", msg->stamp.sec); 
  ROS_INFO("recieve msg.stamp.nsec = %d", msg->stamp.nsec);
  ROS_INFO("recieve msg.data = %d", msg->data);
}

int main(int argc, char **argv)
{
  // 노드 네임 초기화: 특별히 이름을 지정하지 않고 노드를 실행하면 "/topic_subscriber" 란 네임을 갖게 된다.
  ros::init(argc, argv, "topic_subscriber");
  // Node handle declaration for communication with ROS system
  ros::NodeHandle nh;

  // 서브스크라이버 선언: 'MsgTutorial' 타입의 메시지를 구독하는 객체 'ros_tutorial_sub'를 NodeHandle을 통해 생성
  // 구독 할 토픽 네임: 'ros_tutorial_msg' 
  // 퍼블리셔 큐 사이즈: 100 (100개의 메시지까지 버퍼에 쌓아둘 수 있음)
  // 토픽이 발행될 경우 이를 수신하여 처리하는 콜백 함수 'msgCallback' 등록
  ros::Subscriber ros_tutorial_sub = nh.subscribe("ros_tutorial_msg", 100, msgCallback);

  // 메시지가 수신되기를 대기하다가, 수신되었을 경우 콜백함수를 실행
  ros::spin();
  return 0;
}
```
---

## 6. 노드 빌드 및 실행

### 6.1 빌드 (노드 실행 파일 생성)

```bash
# 캐킨 경로로 이동
$ cd ~/catkin_ws
# 캐킨 빌드 실행: ~/catkin_ws/src 의 모든 패키지 빌드
$ catkin_make
```
빌드 과정에서 나온 출력을 살펴보자. `# !!`은 설명을 위해 덧붙인 주석 표시이다.
```bash
# !! 빌드 설정 출력
Base path: /home/ian/catkin_ws
Source space: /home/ian/catkin_ws/src
Build space: /home/ian/catkin_ws/build
Devel space: /home/ian/catkin_ws/devel
Install space: /home/ian/catkin_ws/install
...
-- Using CATKIN_DEVEL_PREFIX: /home/ian/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /home/ian/catkin_ws/devel;/opt/ros/kinetic
-- This workspace overlays: /home/ian/catkin_ws/devel;/opt/ros/kinetic
-- Using PYTHON_EXECUTABLE: /usr/bin/python
# !! 빌드할 패키지 목록 출력
-- ~~  traversing 13 packages in topological order:
-- ~~  - my_first_ros_pkg
...
-- ~~  - ros_tutorials_topic
-- ~~  - turtlebot3_bringup
-- ~~  - turtlebot3_example
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# !! 기타 cmake 설정 메시지들
...

# !! cmake에서 소스 파일의 연결관계를 확인하고 의존 패키지들도 모두 확인하여 Makefile 생성함
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ian/catkin_ws/build

# !! 이제 빌드 시작
#### Running command: "make -j3 -l3" in "/home/ian/catkin_ws/build"
# !! 기존에 이미 빌드된 패키지들은 변경사항이 없으면 다시 빌드하지 않고 넘어감
Scanning dependencies of target std_msgs_generate_messages_cpp
[  0%] Built target std_msgs_generate_messages_cpp
[  0%] Built target _turtlebot3_msgs_generate_messages_check_deps_VersionInfo
...
[  5%] Built target nav_msgs_generate_messages_nodejs
[  5%] Built target nav_msgs_generate_messages_cpp
[  5%] Built target tf_generate_messages_eus
...
# !! 기존에 빌드되지 않은 타겟들 빌드
...
[ 98%] Linking CXX executable /home/ian/catkin_ws/devel/lib/ros_tutorials_topic/topic_publisher
[100%] Linking CXX executable /home/ian/catkin_ws/devel/lib/ros_tutorials_topic/topic_subscriber
# !! topic_publisher와 topic_subscriber가 빌드가 잘 되었다.
[100%] Built target topic_publisher
[100%] Built target topic_subscriber
```

빌드 결과물들을 확인해보자.
```bash
# build: 빌드를 위한 중간 결과물들이 있다. 
# cmake를 통해 Makefile이 생성된 것을 볼 수 있다.
$ ls ~/catkin_ws/build/ros_tutorials_topic/
catkin_generated  CMakeFiles           CTestTestfile.cmake
cmake             cmake_install.cmake  Makefile

# devel: 빌드를 마치고 생성된 (사용자가 사용할) 결과물만 모여있다.
# devel/include/package_name : 소스코드에서 사용하는 헤더 파일들을 이곳으로 모은다.
# "MsgTutorial.h" 헤더가 생성된 것을 확인할 수 있다.
# 소스코드에서는 이 헤더를 include 하여 메시지 객체를 만들어 전송한다.
$ ls ~/catkin_ws/devel/include/ros_tutorials_topic/
MsgTutorial.h

# devel/lib/package_name : 빌드하여 생성된 실행 파일이나 라이브러리 파일을 이곳으로 모은다.
# "topic_publisher", "topic_subscriber" 두 개의 노드 실행 파일이 생성된 것을 확인할 수 있다.
# rosrun을 실행하면 이곳의 실행 파일들을 검색하여 노드를 실행한다.
$ ls ~/catkin_ws/devel/lib/ros_tutorials_topic/
topic_publisher  topic_subscriber
```

### 6.2 퍼블리셔 실행

다음 명령어로 퍼블리셔를 실행해 보자.  
두 번째 줄은 `ros_tutorial_topic` 패키지의 `topic_publisher` 노드를 실행한다.  
노드 네임은 퍼블리셔 코드에서 설정한대로 `/topic_publisher`로 기본 지정된다.
```bash
# 현재 실행된 마스터가 없다면 마스터 실행
$ roscore
# 새 탭 (ctrl+alt+t) 후
$ rosrun ros_tutorial_topic topic_publisher
```
출력 화면은 다음과 같다.  
퍼블리셔에서 ROS_INFO() 함수를 통해 발행하는 메시지 정보를 프린트 하고 있다.  
```bash
ian@ian:~$ rosrun ros_tutorials_topic topic_publisher 
[ INFO] [1541831179.697112616]: send msg.stamp.sec = 1541831179
[ INFO] [1541831179.697172543]: send msg.stamp.nsec = 697069994
[ INFO] [1541831179.697192040]: send msg.data = 0
[ INFO] [1541831179.797259465]: send msg.stamp.sec = 1541831179
[ INFO] [1541831179.797313766]: send msg.stamp.nsec = 797227852
[ INFO] [1541831179.797332169]: send msg.data = 1
[ INFO] [1541831179.897833911]: send msg.stamp.sec = 1541831179
[ INFO] [1541831179.897876527]: send msg.stamp.nsec = 897801549
[ INFO] [1541831179.897889909]: send msg.data = 2
[ INFO] [1541831179.999185339]: send msg.stamp.sec = 1541831179
[ INFO] [1541831179.999225632]: send msg.stamp.nsec = 999153431
[ INFO] [1541831179.999239483]: send msg.data = 3
[ INFO] [1541831180.097754614]: send msg.stamp.sec = 1541831180
[ INFO] [1541831180.097801286]: send msg.stamp.nsec = 97718615
...
```
`ros_tutorial_msg` 토픽을 확인하기 위해 우선 현재 발행중인 토픽 목록을 확인한다.
```bash
$ rostopic list
/ros_tutorial_msg
/rosout
/rosout_agg
```
`/ros_tutorial_msg` 토픽이 발행 중임을 알 수 있다. 그렇다면 발행되는 메시지 내용을 확인해보자.
```bash
$ rostopic echo /ros_tutorial_msg
stamp: 
  secs: 1541831573
  nsecs:   7214567
data: 3369
---
stamp: 
  secs: 1541831573
  nsecs: 106731134
data: 3370
---
stamp: 
  secs: 1541831573
  nsecs: 207368135
data: 3371
---
...
```
`/ros_tutorial_msg` 토픽으로 메시지들이 네트워크 상으로 발행되고 있음을 확인할 수 있다.

### 6.3 서브스크라이버 실행

다음 명령어로 서브스크라이버를 실행해 보자.
`ros_tutorial_topic` 패키지의 `topic_subscriber` 노드를 실행한다.  
노드 네임은 서브스크라이버 코드에서 설정한대로 `/topic_subscriber`로 기본 지정된다.  
```bash
# 새 탭 (ctrl+alt+t) 후
$ rosrun ros_tutorials_topic topic_subscriber
```
출력 화면은 다음과 같다.  
서브스크라이버 노드에서 수신 받은 데이터를 ROS_INFO() 함수를 통해 메시지를 프린트 하고 있다.  

```bash
[ INFO] [1541832480.410315224]: recieve msg.stamp.sec = 1541832480
[ INFO] [1541832480.410366307]: recieve msg.stamp.nsec = 409756761
[ INFO] [1541832480.410380701]: recieve msg.data = 12443
[ INFO] [1541832480.507663466]: recieve msg.stamp.sec = 1541832480
[ INFO] [1541832480.507707152]: recieve msg.stamp.nsec = 507270214
[ INFO] [1541832480.507721908]: recieve msg.data = 12444
[ INFO] [1541832480.607211223]: recieve msg.stamp.sec = 1541832480
[ INFO] [1541832480.607241362]: recieve msg.stamp.nsec = 606816000
[ INFO] [1541832480.607257491]: recieve msg.data = 12445
...
```
`rqt_graph` 명령어를 통해 노드와 메시지의 연결 관계를 확인할 수 있다.  

![img](./assets/tutorials_topic_graph.png)

