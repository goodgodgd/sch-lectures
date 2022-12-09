#!/home/ian/.pyenv/versions/ros_py36/bin/python
# 사용자명(ian) 교체!
import rospy
from sensor_msgs.msg import Image
import cv2
import os
import numpy as np


def image_to_sensor_msg(image):
    sensor_img = Image()
    sensor_img.header.seq = 0
    sensor_img.header.stamp = rospy.get_rostime()
    sensor_img.header.frame_id = ""
    sensor_img.height = image.shape[0]
    sensor_img.width = image.shape[1]
    # channel이나 depth가 없으니 step을 대신 사용
    sensor_img.step = image.shape[2]
    sensor_img.encoding = f"{image.dtype}"
    sensor_img.data = image.tostring()
    return sensor_img


def main():
    rospy.init_node("image_publisher")
    pub = rospy.Publisher("np_image", Image, queue_size=1)

    filepath = os.path.abspath(__file__)
    pkgpath = os.path.dirname(os.path.dirname(filepath))
    print(f"this file: {filepath} \npackage path: {pkgpath}")
    image = cv2.imread(pkgpath + "/ros.jpeg")

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        image = cv2.flip(image, 1)
        msg = image_to_sensor_msg(image)
        pub.publish(msg)
        print(f"publish image, time={msg.header.stamp.to_sec() % 1000:.1f}, w={msg.width}, h={msg.height}")
        rate.sleep()


if __name__ == "__main__":
    main()

