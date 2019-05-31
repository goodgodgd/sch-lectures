#ifndef TB3DRIVER_H
#define TB3DRIVER_H

#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>
#include <string>

class TB3Driver
{
public:
    TB3Driver();
    void ldsCallback(const sensor_msgs::LaserScan::ConstPtr& scan);
    geometry_msgs::Twist getVelocity();

private:
    geometry_msgs::Twist selfDrive(const sensor_msgs::LaserScan::ConstPtr& scan);

    ros::Publisher* pubVelo;
    geometry_msgs::Twist velMsg;
    sensor_msgs::LaserScan curScan;
};

#endif // TB3DRIVER_H
