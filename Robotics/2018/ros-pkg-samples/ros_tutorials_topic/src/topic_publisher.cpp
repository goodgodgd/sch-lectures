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

  // 퍼블리셔 선언: 'MsgTutorial' 타입의 메시지를 발행하는 객체 
  // 'ros_tutorial_pub'를 NodeHandle을 통해 생성
  // 발행 할 토픽 네임: 'ros_tutorial_msg' 
  // 퍼블리셔 큐 사이즈: 100 (100개의 메시지까지 버퍼에 쌓아둘 수 있음)
  ros::Publisher ros_tutorial_pub = 
  	nh.advertise<ros_tutorials_topic::MsgTutorial>
      ("ros_tutorial_msg", 100);

  // loop 빈도 설정, 초당 10번의 loop 반복
  ros::Rate loop_rate(10);

  // 메시지 데이터 객체 생성
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

