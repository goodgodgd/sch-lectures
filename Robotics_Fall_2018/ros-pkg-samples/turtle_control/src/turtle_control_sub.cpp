#include <ros/ros.h>
#include <turtlesim/Pose.h>

void poseCallback(const turtlesim::Pose::ConstPtr& pose)
{
    static int count = 0;
    ROS_INFO("receive count = %d", count++);
    ROS_INFO("received pose.position = (%f, %f, %f)", pose->x, pose->y, pose->theta);
}

int main(int argc, char **argv)
{
    // set node default name: 특별히 이름을 지정하지 않고 노드를 실행하면 "/turtle_control_sub" 란 name을 갖게 된다.
    ros::init(argc, argv, "turtle_control_sub");
    // Node handle declaration for communication with ROS system
    ros::NodeHandle nh;

    // subscriber 선언: 'turtlesim::Pose' 타입의 메시지를 수신하는 객체
    // 'pose_sub'을 NodeHandle을 통해 생성
    // 구독 할 topic name: 'pose' (turtlesim_node에서 subscribe하는 topic 이름)
    // subscriber queue size: 10 (10개의 메시지까지 버퍼에 쌓아둘 수 있음)
    ros::Subscriber pose_sub = nh.subscribe<turtlesim::Pose>("pose", 10, poseCallback);

    ros::spin();
    return 0;
}
