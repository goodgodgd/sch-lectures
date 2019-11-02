#!/path/to/venv/bin/python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class SelfDrive:
    def __init__(publisher):
        self.publisher = publisher

    def lds_callback(scan):
        # scan 분석 후 속도 결정
        # ...
        turtle_vel = Twist()
        # 전진 속도 및 회전 속도 지정
        turtle_vel.linear.x = 0.1
        turtle_vel.angular.z = 0.2
        # 속도 출력
        publisher.publish(turtle_vel)

rospy.init_node('self_drive')
publisher = rospy.Publisher('cmd_vel', TimePose, queue_size=1)
driver = SelfDrive(publisher)
subscriber = rospy.Subscriber('scan', LaserScan, 
                              lambda scan: driver.lds_callback(scan))
rospy.spin()

