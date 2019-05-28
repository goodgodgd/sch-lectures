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

  // 서브스크라이버 선언: 'MsgTutorial' 타입의 메시지를 구독하는 객체 
  // 'ros_tutorial_sub'를 NodeHandle을 통해 생성
  // 구독 할 토픽 네임: 'ros_tutorial_msg' 
  // 퍼블리셔 큐 사이즈: 100 (100개의 메시지까지 버퍼에 쌓아둘 수 있음)
  // 토픽이 발행될 경우 이를 수신하여 처리하는 콜백 함수 'msgCallback' 등록
  ros::Subscriber ros_tutorial_sub = nh.subscribe("ros_tutorial_msg", 100, msgCallback);

  // 메시지가 수신되기를 대기하다가, 수신되었을 경우 콜백함수를 실행
  ros::spin();
  return 0;
}
