# ROS Command

### Example scenario

강의 자료 상의 주요 명령어들을 확인할 수 있는 예제

#### turtlesim 실행
```
# turtlesim 패키지 경로 갔다 오기
$ roscd turtlesim
$ cd ~

# 마스터 실행
$ roscore

# 새 탭 (ctrl + shift + t), 터틀봇 시뮬레이터 실행
$ rosrun turtlesim turtlesim_node

# 새 탭 (ctrl + shift + t), 터틀봇 원격조종 노드 실행
$ rosrun turtlesim turtle_teleop_key

# 새 탭 (ctrl + shift + t), ros graph를 볼수 있는 rqt_graph 실행
$ rosrun rqt_graph rqt_graph
```

#### 현재 가동중인 구성 요소 확인

명령어
```
# 새 창 (ctrl + alt + t)
# lists of nodes, topics, service, parameters
$ rosnode list
$ rostopic list
$ rosservice list
$ rosparam list
```

결과
```
ian@ian:~$ rosnode list
/rosout
/rqt_gui_py_node_16177
/teleop_turtle
/turtlesim

ian@ian:~$ rostopic list
/rosout
/rosout_agg
/statistics
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose

ian@ian:~$ rosservice list
/clear
/kill
/reset
/rosout/get_loggers
/rosout/set_logger_level
/rqt_gui_py_node_16177/get_loggers
/rqt_gui_py_node_16177/set_logger_level
/spawn
/teleop_turtle/get_loggers
/teleop_turtle/set_logger_level
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
/turtlesim/get_loggers
/turtlesim/set_logger_level

ian@ian:~$ rosparam list
/background_b
/background_g
/background_r
/rosdistro
/roslaunch/uris/host_localhost__43835
/rosversion
/run_id
```

#### 가동중인 요소들의 정보 확인

명령어
```
# info of nodes, topics, service, parameters
$ rosnode info turtlesim
$ rostopic info /turtle1/pose
$ rostopic type /turtle1/cmd_vel
$ rosservice info /turtle1/pose
$ rosservice type /turtle1/teleport_absolute
$ rosparam get /background_b
```

결과
```
ian@ian:~$ rosnode info turtlesim
--------------------------------------------------------------------------------
Node [/turtlesim]
Publications: 
 * /rosout [rosgraph_msgs/Log]
 * /turtle1/color_sensor [turtlesim/Color]
 * /turtle1/pose [turtlesim/Pose]
Subscriptions: 
 * /turtle1/cmd_vel [geometry_msgs/Twist]
Services: 
 * /clear
 * /kill
 * /reset
 * /spawn
 * /turtle1/set_pen
 * /turtle1/teleport_absolute
 * /turtle1/teleport_relative
 * /turtlesim/get_loggers
 * /turtlesim/set_logger_level
contacting node http://localhost:43951/ ...
Pid: 11179
Connections:
 * topic: /rosout
    * to: /rosout
    * direction: outbound
    * transport: TCPROS
 * topic: /turtle1/cmd_vel
    * to: /teleop_turtle (http://localhost:45693/)
    * direction: inbound
    * transport: TCPROS

ian@ian:~$ rostopic info /turtle1/pose
Type: turtlesim/Pose
Publishers: 
 * /turtlesim (http://localhost:43951/)
Subscribers: None

ian@ian:~$ rostopic type /turtle1/cmd_vel 
geometry_msgs/Twist

ian@ian:~$ rosservice info /turtle1/set_pen
Node: /turtlesim
URI: rosrpc://localhost:58967
Type: turtlesim/SetPen
Args: r g b width off

ian@ian:~$ rosservice type /turtle1/teleport_absolute 
turtlesim/TeleportAbsolute

ian@ian:~$ rosparam get /background_b
255
```

#### 발행중인 토픽 읽어오기

명령어
```
$ rostopic echo /turtle1/pose
# 이후 turtle_teleop_key 에서 방향키로 거북이를 제어하며 pose 확인
```

결과
```
...
x: 8.70827102661
y: 7.36393070221
theta: -2.22044604925e-16
linear_velocity: 0.0
angular_velocity: 0.0
...
```

#### 서비스 메시지 보내기

명령어
```
$ rosservice args /turtle1/set_pen
$ rosservice call /turtle1/set_pen 255 0 0 5 0
# 이후 turtle_teleop_key 에서 방향키로 거북이를 움직이면 
# 기존 경로는 그대로고 새 경로는 빨간색으로 표시됨
```

결과
```
ian@ian:~$ rosservice args /turtle1/set_pen
r g b width off
```

#### 토픽을 파일로 저장하고 재생

명령어
```
rosbag record /turtle1/cmd_vel
rosbag info 2018-11-04-00-00-57.bag
rosbag play 2018-11-04-00-00-57.bag
```

```
ian@ian:~$ rosbag record /turtle1/cmd_vel
[ INFO] [1541257257.987679341]: Subscribing to /turtle1/cmd_vel
[ INFO] [1541257257.993879724]: Recording to 2018-11-04-00-00-57.bag.

ian@ian:~$ rosbag info 2018-11-04-00-00-57.bag 
path:        2018-11-04-00-00-57.bag
version:     2.0
duration:    22.5s
start:       Nov 04 2018 00:01:03.02 (1541257263.02)
end:         Nov 04 2018 00:01:25.50 (1541257285.50)
size:        8.2 KB
messages:    23
compression: none [1/1 chunks]
types:       geometry_msgs/Twist [9f195f881246fdfa2798d1d3eebca84a]
topics:      /turtle1/cmd_vel   23 msgs    : geometry_msgs/Twist

ian@ian:~$ rosbag play 2018-11-04-00-00-57.bag 
[ INFO] [1541257341.208936194]: Opening 2018-11-04-00-00-57.bag
Waiting 0.2 seconds after advertising topics... done.
Hit space to toggle paused, or 's' to step.
 [DELAYED]  Bag Time: 1541257263.020857   Duration: 0.000000 / 22.479988   Delay
 [RUNNING]  Bag Time: 1541257263.020857   Duration: 0.000000 / 22.479988         
 [RUNNING]  Bag Time: 1541257263.020857   Duration: 0.000000 / 22.479988         
 [RUNNING]  Bag Time: 1541257263.021007   Duration: 0.000150 / 22.479988         
 [RUNNING]  Bag Time: 1541257263.121247   Duration: 0.100390 / 22.479988         
 [RUNNING]  Bag Time: 1541257263.221361   Duration: 0.200504 / 22.479988         
 [RUNNING]  Bag Time: 1541257263.322173   Duration: 0.301316 / 22.479988         
 ...
```

