# Import a ROS Workspace into QtCreator

간단한 소스코드는 메모장에서 작성해도 되지만 복잡한 알고리즘을 구현하기 위해서는  통합개발환경(IDE)가 필수다. 개발환경에서 제공하는 자동완성기능과 문법체크를 활용할 수 있어야 코딩의 불확실성이 줄어들고 개발이 편리해진다. 여기서는 QtCreator 환경에서 ROS 패키지를 개발하는 방법을 알아본다.

## 1. Install ROS QtCreator plugin

원래는 [이곳](https://ros-industrial.github.io/ros_qtc_plugin/_source/How-to-Install-Users.html) 에서 받아야하는데 요즘 서버가 작동하지 않아서 받을 수 없다.  
그래도 저자가 따로 알려준 ftp 서버에서는 받을 수 있다. 
https://qtcreator-ros.datasys.swri.edu/downloads/installers/xenial/

설치하는 방법은 다음과 같다.
```bash
$ cd Downloads
$ wget https://qtcreator-ros.datasys.swri.edu/downloads/installers/xenial/qtcreator-ros-xenial-latest-offline-installer.run
$ sudo ./qtcreator-ros-xenial-latest-offline-installer.run
```
설치 경로는 기존에 설치된 qtcreator 옆에 다른 폴더를 만들어 지정한다.
`/opt/Qt5.11.1/Tools/QtCreatorRosPlugin`  

설치후 qt로 앱을 검색해보면 두 개의 qtcreator가 보일 것이다.  
그중 `Qt Creator (4.5.1)`이라 된 것을 실행시키고 런처(사이드바)에 고정시키자.  

## 2. Prepare packages

수업 github에 있는 패키지 파일들을 캐킨 워크스페이스로 옮겨 빌드해본다.
```bash
#없으면 코드를 받고 미리 받아놨다면 cd로 경로이동만 한다.
$ git clone https://github.com/goodgodgd/Fall_2018_Lectures.git
$ cd Fall_2018_Lectures/Robotics/ros-pkg-samples
#패키지 파일들이 들어있는 ros-pkg-samples 폴더의 소프트링크(바로가기)를 catkin_ws에 만든다.
$ chmod a+x link_sources.sh
$ cd ~/catkin_ws
#ros-pkg-samples 가 있는지 확인
$ ls src
CMakeLists.txt  ros-pkg-samples  turtlebot3  turtlebot3_msgs
#패키지 빌드
$ catkin_make
#패키지 작동 확인
$ rosrun ros_tutorials_topic topic_publisher
```

## 3. Import ROS Project

catkin_ws에 있는 모든 패키지들을 한번에 불러온다.
자료 원문 참조: https://ros-industrial.github.io/ros_qtc_plugin/_source/Import-ROS-Workspace.html

1. QtCreator 오른쪽의 `Welcom` 버튼
2. +New Project -> Other Project -> ROS Workspace
3. 이름은 아무거나 짓고 (e.g. ian_ros_ws) `Workspace_Path`를 지정한다. (~/catkin_ws)

(import가 잘 안되면 빌드 옵션에서 catkin_make를 catkin_tools로 바꿔본다??)

불러오고 나면 일반 qt-project들 처럼 `ctrl+b`를 하면 빌드가 된다.  
하지만 `ctrl+r`을 눌러도 실행은 되지 않는다.  
노드 실행은 `roscore` 이후 `rosrun`으로 실행한다.

