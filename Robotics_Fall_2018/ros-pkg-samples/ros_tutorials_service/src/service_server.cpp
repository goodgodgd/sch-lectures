// ROS Default Header File
#include "ros/ros.h"
// SrvTutorial Service Header. 빌드시 SrvTutorial.srv 파일로부터 자동 생성됨
#include "ros_tutorials_service/SrvTutorial.h"

// 서비스 요청이 들어왔을 때 실행되는 함수
// 클라이언트에서 서비스 요청시 보낸 데이터 타입은 
// 'SrvTutorial'로서 내부 변수로 request와 response를 갖고 있었는데
// 서버에서 받을 때는 'SrvTutorial'로 한번에 받지 않고
// request와 response를 각각 따로 받는다.
bool calculation(ros_tutorials_service::SrvTutorial::Request &req,
                 ros_tutorials_service::SrvTutorial::Response &res)
{
// req를 reference type으로 받아서 데이터 복사를 안해도 되고
// res를 reference type으로 받아서 연산한 결과를 외부로 출력할 수 있다.

  // 클라이언트에서 보낸 a와 b 값을 더하여 결과 값을 res.result에 저장
  res.result = req.a + req.b;

  // 서비스 요청으로 보낸 값과 서비스 응답 값을 출력한다.
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: %ld", (long int)res.result);

  return true;
}

int main(int argc, char **argv)
{
  // 노드 네임 초기화: 특별히 이름을 지정하지 않고 노드를 실행하면 "/service_server" 란 네임을 갖게 된다.
  ros::init(argc, argv, "service_server");
  // Node handle declaration
  ros::NodeHandle nh;

  // 서비스 서버 선언: 'SrvTutorial' 타입의 서비스 요청을 처리하는 객체 
  // 'ros_tutorials_service_server'을 NodeHandle을 통해 생성
  // 요청을 받을 서비스 네임: 'ros_tutorial_srv'
  // 요청을 처리할 콜백 함수: 'calculation'
  ros::ServiceServer ros_tutorials_service_server = nh.advertiseService("ros_tutorial_srv", calculation);
  ROS_INFO("ready srv server!");

  // 서비스 요청을 기다린다.
  ros::spin();
  return 0;
}

