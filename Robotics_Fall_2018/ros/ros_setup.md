# ROS 설치 가이드

일반적으로 터틀봇을 ROS를 이용해 제어할 때 Remote PC와 SBC 두 PC가 사용된다. 
- Remote PC: 원격에서 연산을 하고 제어를 하는 PC다. 데스크탑이나 랩탑이 주로 그 역할을 한다.
- SBC: 로봇과 직접 연결된 소형 PC다. 우리의 경우 라즈베리파이가 그 역할을 한다.  

라즈베리파이와 같은 SBC는 연산속도가 느려 복잡한 알고리즘을 수행하기에 적절하지 않다.  
SBC는 Remote PC에 센서 데이터를 전달해주고 Remote PC에서 오는 하드웨어 제어 신호를 실행해주는 역할만 하는 것이 일반적이다.  
따라서 ROS는 Remote PC와 SBC 모두 설치해 줘야한다.  
아래는 각각의 PC에 대한 ROS 설치 및 설정 방법이다.

### 1. PC Setup

원문: http://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/#pc-setup  
***

#### 1.1 우분투 설치

우분투 설치는 예전에 [여기](https://github.com/goodgodgd/Fall_2018_Lectures/blob/master/Robotics/linux-basic/00_LinuxInstallation.md) 
소개한 대로 가상 머신으로 설치한다.  
가이드에 나와있는 우분투 버전이 16.04 이므로 이 버전을 설치한다.  
유의할 점은 네트워크 설정이다. ROS가 직접 와이파이에 접속해야 하므로 기본 가상 머신의 네트워크 설정으로는 원격 통신이 되지 않는다.  
다음과 같이 네트워크 설정을 실행한다.   
1. Virtual Box를 실행한다.
2. 가상 머신 이름을 우클릭하고 '설정'으로 들어간다.
3. '네트워크'에서 '다음에 연결됨(A):' 옆의 옵션을 '어댑터에 브리지'로 설정한다.

***

#### 1.2 ROS 설치

설치 스크립트를 다운 받아 스크립트를 실행한다.
```bash
$ sudo apt update
$ sudo apt upgrade
$ cd Downloads
$ wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh
```
설치 스크립트는 대략 다음과 같은 기능을 한다. 
- ros-desktop-full 설치
- catkin workspace를 만드는 작업
- ROS 환경설정: ~/.bashrc 수정

설치가 다 되어 "Complete!!!" 가 뜨면 **PC 리부트**
***

#### 1.3 네트워크 설정

- `gedit ~/.bashrc` 명령으로 .bashrc 파일을 열어보면 아래쪽에 ros 설치과정에서 추가된 스크립트가 있다.  
- 맨 아래를 보면 두 개의 주소를 볼 수 있다.
    - `ROS_MASTER_URI` : 여러대의 PC가 통신하는 경우 한 PC가 master 역할을 해줘야한다. `ROS_MASTER_URI`는 master PC의 IP 주소이다.  
    - `ROS_HOSTNAME` : ROS Node의 주소에 들어간다. 자기 자신의 IP를 쓴다.  

- 기본 설정은 하나의 PC안에서 모든 동작을 하는 것이므로 두 주소 모두 `localhost`로 되어있다.  
- 그러나 터틀봇의 SBC와 통신을 하기 위해서는 이를 IP 주소로 바꿔야 한다.  
- IP 주소는 `ifconfig` 명령어를 이용해 확인할 수 있다.  
    ```bash
    ian@ian:~/workplace/Fall_2018_Lectures$ ifconfig
    enp0s3    Link encap:Ethernet  HWaddr 08:00:27:fb:32:71  
              inet addr:192.168.0.49  Bcast:192.168.0.255  Mask:255.255.255.0
              inet6 addr: fe80::b363:d11b:79f9:924a/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:3090176 errors:0 dropped:0 overruns:0 frame:0
              TX packets:719554 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:4612766528 (4.6 GB)  TX bytes:51164375 (51.1 MB)
    
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:65536  Metric:1
              RX packets:3956 errors:0 dropped:0 overruns:0 frame:0
              TX packets:3956 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:510356 (510.3 KB)  TX bytes:510356 (510.3 KB)
    ```
- 출력에서 `inet addr:192.168.xxx.xxx` 로 시작하는 주소를 찾아 쓴다.    
- Remote PC가 master 역할을 하니 `ROS_MASTER_URI`, `ROS_HOSTNAME` 둘 다 같은 주소를 쓴다.  
- 다음은 설정 예시이다.
    ```bash
    export ROS_MASTER_URI=http://192.168.0.49:11311
    export ROS_HOSTNAME=192.168.0.49
    ```
***

#### 1.4 터틀봇 제어 패키지 설치

터틀봇을 제어할 수 있는 패키지를 설치한다.
저장소에 없는 패키지는 소스를 받아 catkin 으로 빌드한다.

```bash
$ sudo apt install ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers
$ cd ~/catkin_ws/src/
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
$ cd ~/catkin_ws && catkin_make
```

그리고 .bashrc 에서 추가해야 할 스크립트가 한줄 더 있다.
```bash
export TURTLEBOT3_MODEL=burger 
```
이걸 추가해야 turtlebot3 패키지에서 정확한 제어대상을 알 수 있다.

***

#### 1.5 ROS 동작 테스트

거북이와 놀아보세요.
```bash
$ roscore
$ rosrun turtlesim turtlesim_node
$ rosrun turtlesim turtle_teleop_key
$ rosrun rqt_graph rqt_graph
```

***

### 2. SBC Setup

원문: http://emanual.robotis.com/docs/en/platform/turtlebot3/raspberry_pi_3_setup/#raspberry-pi-3-setup

- 용어정리
    - SBC: Single Board Computer의 약자로 하나의 보드 위에 프로세서, 메모리, 저장장치 등을 모아 
    PC처럼 작동할 수 있는 장치. 여기서는 SBC 중 하나인 `Raspberry Pi 3`를 터틀봇에 올려 터틀봇을
    제어하는데 사용한다. 
    - Raspberry Pi 3: 라즈베리 파이는 영국 잉글랜드의 라즈베리 파이 재단이 학교와 개발도상국에서 
    기초 컴퓨터 과학의 교육을 증진시키기 위해 개발한 신용카드 크기의 싱글 보드 컴퓨터이다. (위키)  
    자세한 내용은 홈페지이 참조: https://www.raspberrypi.org/downloads/raspbian/
    - Raspbian: 라즈비안은 라즈베리 파이의 개발사에서 만든 OS이자 공식 라즈베리 파이용 OS으로 
    데비안 리눅스를 기반으로 만들어진 배포판이다.
- 로보티즈 e-manual에서 라즈베리파이 하드웨어에 설치 할 수 있는 운영체제는 두 가지가 있다.  
    - `Raspbian`와 `Ubuntu 16.04 MATE` (메이트 아니고 마테) 이다.  
    - 우분투 마테는 우분투에서 사용자 환경을 좀 다르게 바꾼 것인데 결과적으로 라즈비안을 설치할 것을 권장한다.  
    - 둘 다 설치방법은 똑같은데 로보티즈에서 기본 라즈비안에 ROS 패키지를 다 설치한 버전을 제공한다.  
    (기본 라즈비안을 설치하여 Remote PC처럼 설치할 수도 있다.)  


#### 2.1 Raspbian 설치

라즈비안 설치 방법은 다음과 같다.
- [여기](http://www.robotis.com/service/download.php?no=730)에서 설치 파일을 다운받는다.
- [여기](https://etcher.io/) 에서 etcher를 다운 받는다.
- etcher 압축 파일을 압축 해제하고 실행한다.
    - 탐색기에서 Downloads 폴더로 들어가 `etcher-electron-1.4.5-linux-x64.zip` 압축파일을 우클릭하고 'Extract here'를 누르면 압축해제된 실행파일이 생긴다.
    - 실행파일을 더블클릭하면 설치할까요? 에 'yes'로 대답하면 실행된다.
- `Select image': 다운받은 라즈비안 이미지를 선택한다.
- 'Select drive': SD 카드를 USB를 통해 연결하고 드라이브를 선택한다.
- 'Burn'을 누르면 설치가 된다.

이후 사용방법
- SBC에 SD 카드, 모니터, 키보드, 마우스를 연결하고 전원을 켠다.  
- 기본 사용자명은 **pi**, 비밀번호는 **turtlebot** 이다.
- 오른쪽 상단의 메뉴를 이용해 무선 인터넷에 연결할 수 있다.
***

#### 2.2 파티션 확장

1. 기본 설정  
    기본 파티션은 설치된 패키지들로 남은 용량이 없다. SD카드의 남은 용량을 활용할 수 있도록 파티션을 넓혀줘야 한다.  
    로보티즈 매뉴얼에는 간단한 커맨드 명령어로 이를 할 수 있는 방법이 나와있다.
    ```bash
    $ sudo raspi-config
      (select 7 Advanced Options > A1 Expand Filesystem)
    ```

2. 다른 설정 (swap 메모리 할당)  
    그런데 라즈베리파이 하드웨어에 메모리 용량이 1GB 밖에 되지 않아 연산을 처리하는데 좀 부족할 수 있다.  
    **위 방법 대신** gparted를 이용하면 SD 카드에 swap 메모리를 할당할 수 있다.  
    swap 메모리는 저장장치의 메모리를 RAM 처럼 쓸 수 있게 해준다.  
    SD 카드에 swap 메모리를 할당하여 부족한 메모리 용량을 보충해보자. (옵션)
    - 인터넷을 연결하고 `gparted` 를 설치한다.
        ```bash
        sudo apt update
        sudo apt install gparted
        ```
    - 커맨드에서 `sudo gparted`를 실행한다.
    - 현재 파티션을 우클릭하여 'Resize/Move'를 선택한다.
    - 2GB만 남기고 SD 카드의 용량을 모두 할당한다.
    - 남은 2GB 자리에 우클릭하여 'New'를 선택한다.
    - 'File system: linux-swap' 을 선택하고 남은 용량을 할당하여 'Add'를 누른다.
    
    상단의 체크표시 (Apply all operations)를 누르면 파티션 재조정이 이루어진다.
***

#### 2.3 펌웨어 및 패키지 업데이트

출처: https://discourse.ros.org/t/announcing-turtlebot3-software-v1-0-0-and-firmware-v1-2-0-update/4888

[SBC]에서
```bash
#opencr 업데이트
$ export OPENCR_PORT=/dev/ttyACM0
$ export OPENCR_MODEL=burger
$ rm -rf ./opencr_update.tar.bz2

#한 줄의 명령어
$ wget https://github.com/ROBOTIS-GIT/OpenCR/raw/master/arduino/opencr_release/shell_update/opencr_update.tar.bz2 && tar -xvf opencr_update.tar.bz2 && cd ./opencr_update && ./update.sh $OPENCR_PORT $OPENCR_MODEL.opencr && cd ..
#여기까지

#패키지 소스 지우고 다시 다운로드
$ cd ~/catkin_ws/src/
$ rm -rf turtlebot3/ turtlebot3_msgs/ hls_lfcd_lds_driver/
$ git clone https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git

#터틀봇에 불필요한 노드 삭제
$ cd ~/catkin_ws/src/turtlebot3
$ sudo rm -r turtlebot3_description/ turtlebot3_teleop/ turtlebot3_navigation/ turtlebot3_slam/ turtlebot3_example/

#기존 빌드파일 삭제 후 다시 빌드
$ cd ~/catkin_ws/
$ rm -rf build/ devel/
$ cd ~/catkin_ws && catkin_make -j1
```

#### 2.4 시간 설정

두 개의 PC가 ROS를 통해 통신을 하기 위해서는 시간을 동기화 해줘야 한다.
```bash
sudo apt install ntpdate
sudo ntpdate ntp.ubuntu.com
```
***

#### 2.5 네트워크 설정

Remote PC (1.3)와 마찬가지로 라즈비안에서도 `.bashrc`에 있는 IP 설정을 수정한다.
- `ifconfig` 명령어를 입력한다.
- 출력에서 `inet addr:192.168.xxx.xxx` 로 시작하는 주소를 찾아 메모한다. 
- `leafpad ~/.bashrc` 명령으로 파일을 연다.
- 맨 아래 `ROS_MASTER_URI`와 `ROS_HOSTNAME`의 `localhost`를 IP 주소로 수정한다.  
- `ROS_MASTER_URI`에는 **Remote PC**의 IP 주소를 쓴다.
- `ROS_HOSTNAME`에는 SBC의 IP 주소를 쓴다.
    - IP 주소는 `ifconfig` 명령어를 입력하여 출력에서 `inet addr:192.168.xxx.xxx` 로 시작하는 주소를 찾아 쓴다. 
    - 기존
        ```bash
        export ROS_MASTER_URI=http://localhost:11311
        export ROS_HOSTNAME=localhost
        ```
    - 수정 후 (예시)
        ```bash
        export ROS_MASTER_URI=http://192.168.0.49:11311
        export ROS_HOSTNAME=192.168.0.30
        ```
- 저장 후 leafpad 를 닫는다.
- 설정을 적용하기 위해 다음 명령어를 실행한다.

    - `source ~/.bashrc`
***

#### 2.6 원격 제어 확인

Remote PC에서 ssh 명령어로 SBC의 터미널에 접속할 수 있다.
아래 명령어를 입력하고 SBC의 비밀번호 (기본: turtlebot) 를 입력하면 터미널상의 사용자명이 `pi`로 바뀐다.

```bash
#192.168.xxx.xxx 는 SBC의 IP 주소 == 2.4의 ROS_HOSTNAME
$ ssh pi@192.168.xxx.xxx

#로봇에서 odometry와 lds 메시지 토픽 발행
pi@raspberrypi $ roslaunch turtlebot3_bringup turtlebot3_robot.launch

#새 탭 (ctrl+shit+T), 터틀봇을 원격 조종할 수 있는 노드 실행
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch –screen

#새 탭 (ctrl+shit+T), 터틀봇의 경로와 LiDAR 정보를 볼 수 있는 rqt 실행
$ roslaunch turtlebot3_bringup turtlebot3_model.launch
```
이제 SBC에 모니터, 키보드, 마우스가 없어도 원격 접속을 통해 SBC를 제어 할 수 있다.  
단지 커맨드로만 제어할 수 있어 약간 불편할 수는 있지만 어차피 SBC에서 해야하는 건 ROS를 활성화 명령어를 내리는 것 뿐이다.  