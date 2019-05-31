#include "self_drive/tb3driver.h"

TB3Driver::TB3Driver()
{
	velMsg.linear.x = 0; velMsg.linear.y = 0; velMsg.linear.z = 0;
	velMsg.angular.x = 0; velMsg.angular.y = 0; velMsg.angular.z = 0;
}

void TB3Driver::ldsCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
	// copy before processing for data time sync
	velMsg = selfDrive(scan);
}

geometry_msgs::Twist TB3Driver::selfDrive(const sensor_msgs::LaserScan::ConstPtr& scan)
{
	geometry_msgs::Twist vel;
	vel.linear.x = 0; vel.linear.y = 0; vel.linear.z = 0;
	vel.angular.x = 0; vel.angular.y = 0; vel.angular.z = 0;

	// TODO: write some algorithm to move to target avoding obstacles
	// vel.linear.x = 0.7; vel.angular.z= 1.0;
	ROS_INFO("selfDrive first = %.3f, %.3f", scan->ranges[0], scan->ranges[359]);
	return vel;
}

geometry_msgs::Twist TB3Driver::getVelocity()
{
    return velMsg;
}
