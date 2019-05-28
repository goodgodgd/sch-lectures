#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>
#include <functional>
#include "self_drive/tb3driver.h"

TB3Driver* tb3driver;

void ldsCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
    ROS_INFO("receive range size = %d, first = %.3f",
             (int)scan->ranges.size(), scan->ranges[0]);
    ROS_INFO("receive inten size = %d, first = %.3f",
             (int)scan->intensities.size(), scan->intensities[0]);
    tb3driver->ldsCallback(scan);
}

int main(int argc, char **argv)
{
	// 노드 네임 초기화
	ros::init(argc, argv, "self_drive");
	// Node handle declaration for communication with ROS system
	ros::NodeHandle nh;
	
	// create publisher: 
    ros::Publisher velopub = nh.advertise<geometry_msgs::Twist>("cmd_vel", 100);
	// set publishing frequency
	ros::Rate loop_rate(10);

    // 반드시 subscriber가 돌아가기 전에 생성
    tb3driver = new TB3Driver(&velopub);
	
	// create subscriber
    ros::Subscriber ldssub = nh.subscribe("scan", 1, ldsCallback);

    while(ros::ok())
    {
        tb3driver->publishVelocity();
        ros::spinOnce();
        loop_rate.sleep();
    }
	return 0;
}

