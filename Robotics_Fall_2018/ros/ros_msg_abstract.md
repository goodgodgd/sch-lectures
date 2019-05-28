# ROS 메시지 통신 요약

`ros_tutorials_topic`과 `ros_tutorials_service`에는 이해를 돕기위해  
소스코드에 많은 주석이 달려있고 부가적인 코드들이 붙어있어서   
코드 구조를 한눈에 파악하기가 쉽지 않다.  
여기서는 메시지 통신을 위한 최소한의 코드만을 표시하여 코드 구조를   
한눈에 파악할 수 있는  요약 코드 예시를 보여주고자 한다.
코드에서 여러 줄이 생략된 경우 `//...`로 표시하였다.

## 1. Topic

### 1.1  topic_puiblisher.cpp

핵심 내용
- 퍼블리셔 객체 생성: `ros::Publisher ros_tutorial_pub = nh.advertise<...>(...)`
- 메시지 발행: `ros_tutorial_pub.publish(msg)`
- 노드와 메시지 네임 설정: `topic_publisher`, `ros_tutorial_msg`
```cpp
// ...
int main(int argc, char **argv)
{
  ros::init(argc, argv, "topic_publisher");
  ros::NodeHandle nh;
  ros::Publisher ros_tutorial_pub = 
  	nh.advertise<ros_tutorials_topic::MsgTutorial>
      ("ros_tutorial_msg", 100);
	// ...
	ros_tutorials_topic::MsgTutorial msg;
	
  while (ros::ok())
  {
		// ...
    ros_tutorial_pub.publish(msg);
    loop_rate.sleep();
  }
}
```

### 1.2  topic_subscriber.cpp

핵심 내용
- 서브스크라이버 객체 생성 및 콜백 함수 등록: `ros::Subscriber ros_tutorial_sub = nh.subscribe(..., msgCallback)`
- 메시지 수신 대기: `ros::spin();`
- 노드와 메시지 네임 설정: `topic_subscriber`, `ros_tutorial_msg`
```cpp
// ...
void msgCallback(const ros_tutorials_topic::MsgTutorial::ConstPtr& msg)
{
  // ... 
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "topic_subscriber");
  ros::NodeHandle nh;
  ros::Subscriber ros_tutorial_sub = nh.subscribe("ros_tutorial_msg", 100, msgCallback);

  ros::spin();
  return 0;
}
```

---



## 2. Service

### 2.1 service_client.cpp

핵심 내용
- 서비스 클라이언트 객체 생성: `ros::ServiceClient ...client = nh.serviceClient<...>`
- 서비스 요청 후 응답 대기: `ros_tutorials_service_client.call(srv)`
- 노드와 서비스 네임 설정: `service_client`, `ros_tutorial_srv`
```cpp
// ...
int main(int argc, char **argv)
{
  ros::init(argc, argv, "service_client");
  ros::NodeHandle nh;
  ros::ServiceClient ros_tutorials_service_client = 
        nh.serviceClient<ros_tutorials_service::SrvTutorial>("ros_tutorial_srv");
	// ...
  if (ros_tutorials_service_client.call(srv))
  {
  	// ...
  }
  // ...
}
```

### 2.2 service_server.cpp

핵심 내용
- 서비스 서버 객체 생성과 콜백 함수 등록: `ros::ServiceServer ...server = nh.advertiseService(..., calculation)`
- 서비스 요청 수신 대기: `ros::spin();`
- 노드와 서비스 네임 설정: `service_server`, `ros_tutorial_srv`
```cpp
// ...
bool calculation(ros_tutorials_service::SrvTutorial::Request &req,
                 ros_tutorials_service::SrvTutorial::Response &res)
{
  res.result = req.a + req.b;
  // ...
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "service_server");
  ros::NodeHandle nh;
  ros::ServiceServer ros_tutorials_service_server = nh.advertiseService("ros_tutorial_srv", calculation);
  ros::spin();
  return 0;
}
```
