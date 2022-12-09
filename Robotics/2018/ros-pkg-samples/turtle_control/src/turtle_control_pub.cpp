#include <ros/ros.h>
#include <geometry_msgs/Twist.h>


int main(int argc, char **argv)
{
    // set node default name: 특별히 이름을 지정하지 않고 노드를 실행하면 "/turtle_control_pub" 란 네임을 갖게 된다.
    ros::init(argc, argv, "turtle_control_pub");
    // Node handle declaration for communication with ROS system
    ros::NodeHandle nh;

    // publisher 선언: 'geometry_msgs::Twist' 타입의 메시지를 발행하는 객체
    // 'cmd_vel_pub'를 NodeHandle을 통해 생성
    // 발행 할 topic name: 'cmd_vel' (turtlesim_node에서 subscribe하는 topic 이름)
    // publisher queue size: 10 (10개의 메시지까지 버퍼에 쌓아둘 수 있음)
    ros::Publisher cmd_vel_pub = nh.advertise<geometry_msgs::Twist>("cmd_vel", 10);

    // loop 빈도 설정, 초당 10번의 loop 반복
    ros::Rate loop_rate(10);

    // 메시지 데이터 객체 생성
    geometry_msgs::Twist vel_msg;
    unsigned int count = 0;

    // ros나 노드 상태에 이상이 생기지 않는 한 무한 반복
    while (ros::ok())
    {
        // 속도 정보 입력
        vel_msg.linear.x = 1.;
        vel_msg.linear.y = 0.;
        vel_msg.linear.z = 0.;
        vel_msg.angular.x = 0.;
        vel_msg.angular.y = 0.;
        vel_msg.angular.z = 0.5;

        // msg 변수 정보 출력
        ROS_INFO("send vel_msg.linear.x = %f at %d", vel_msg.linear.x, count);

        // msg를 발행
        cmd_vel_pub.publish(vel_msg);

        // 앞서 지정한 주기만큼(0.1s) 정지
        loop_rate.sleep();
        count++;
    }
    return 0;
}
