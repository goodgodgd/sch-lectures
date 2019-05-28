// ROS Default Header File
#include "ros/ros.h"
// SrvTutorial Service Header. 빌드시 SrvTutorial.srv 파일로부터 자동 생성됨
#include "ros_tutorials_service/SrvTutorial.h"
// "atoll" 함수를 사용하기 위한 라이브러
#include <cstdlib>

int main(int argc, char **argv)
{
  // 노드 네임 초기화: 특별히 이름을 지정하지 않고 노드를 실행하면 "/service_client" 란 네임을 갖게 된다.
  ros::init(argc, argv, "service_client");

  // 입력 인자는 3개여야 한다. 아래 ROS_INFO 참조
  if (argc != 3)
  {
    ROS_INFO("cmd : rosrun ros_tutorials_service service_client arg0 arg1");
    ROS_INFO("arg0: int64 number, arg1: int64 number");
    return 1;
  }

  // Node handle declaration for communication with ROS system
  ros::NodeHandle nh;

  // 서비스 클라이언트 선언: 'SrvTutorial' 타입의 서비스 요청을 보내는 객체 
  // 'ros_tutorials_service_client'을 NodeHandle을 통해 생성
  // 요청 할 서비스 네임: 'ros_tutorial_srv'
  ros::ServiceClient ros_tutorials_service_client = 
        nh.serviceClient<ros_tutorials_service::SrvTutorial>("ros_tutorial_srv");

  // 서비스 데이터 객체 srv를 생성하고
  // 입력 인자로부터 서비스 리퀘스트 값 입력
  // atoll: 문자열을 숫자로 바꿔주는 함수, char* str -> long long (int64)
  // atoll reference: http://www.cplusplus.com/reference/cstdlib/atoll/
  ros_tutorials_service::SrvTutorial srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);

  // 서비스를 요청 (클라이언트->서버), 요청이 받아들여져 응답이 오면 결과 출력
  if (ros_tutorials_service_client.call(srv))
  {
    ROS_INFO("send srv, srv.Request.a and b: %ld, %ld", (long int)srv.request.a, (long int)srv.request.b);
    ROS_INFO("receive srv, srv.Response.result: %ld", (long int)srv.response.result);
  }
  else  // 요청이 받아들여지지 않으면 에러메시지 출력
  {
    ROS_ERROR("Failed to call service ros_tutorial_srv");
    return 1;
  }
  return 0;
}

