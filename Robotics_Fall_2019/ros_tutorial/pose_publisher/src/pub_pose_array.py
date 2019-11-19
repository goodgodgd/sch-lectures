#!/home/ian/.pyenv/versions/ros_py36/bin/python
# TODO: shebang 경로 수정하기!
import rospy
from std_msgs.msg import Header
from geometry_msgs.msg import Point, Quaternion, Pose, PoseArray
import numpy as np
from pose2d import Pose2D


def pose2d_to_3d(pose2d):
    x, y, theta = pose2d.get_params()
    print("pose2d:", pose2d)
    position = Point(x=x, y=y, z=0)
    orientation = Quaternion(w=np.cos(theta/2), x=0, y=0, z=np.sin(theta/2))
    pose3d = Pose(position=position, orientation=orientation)
    return pose3d


def main():
    rospy.init_node("pub_pose_array")
    publisher = rospy.Publisher("pose_array", PoseArray, queue_size=1)

    center = (1, 0)
    radius = 2
    pose = Pose2D(center[0] + radius * np.cos(0), center[1] + radius * np.sin(0), np.pi / 2)
    angle = np.pi / 18.
    moved = Pose2D(center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle), np.pi / 2 + angle)
    motion = pose.motion_to(moved)
    rate = rospy.Rate(2)
    pose_arr = []
    count = 0
    while not rospy.is_shutdown():
        pose3d = pose2d_to_3d(pose)
        count += 1
        pose3d.position.z = count*0.01
        header = Header(stamp=rospy.get_rostime(), frame_id="map")
        pose_arr.append(pose3d)
        message = PoseArray(header=header, poses=pose_arr)
        publisher.publish(message)
        pose = pose.move(motion)
        rate.sleep()


if __name__ == "__main__":
    main()
