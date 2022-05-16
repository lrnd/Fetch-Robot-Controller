#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, PoseStamped
from std_msgs.msg import Int8

pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
pose = None
status = None

def moveCmd():
    rate = rospy.Rate(10)
    speed = 0.5
    turn = 1.0
    x = 1
    y = 0
    z = 0
    th = 0
    while not rospy.is_shutdown():

        # Control Algorithm Goes Here
        # print(pose)
        if status != None:
            # print(status.data)
            if status.data != 1:
                speed = 0.5
                turn = 1.0
                x = 1
                y = 0
                z = 0
                th = 0
            else:
                speed = 0.5
                turn = 1.0
                x = 0
                y = 0
                z = 0
                th = 0
                rospy.loginfo("Tracking Lost")

            twist = Twist()
            twist.linear.x = x*speed
            twist.linear.y = y*speed
            twist.linear.z = z*speed
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = th*turn
            pub.publish(twist)
            rate.sleep()

def poseCallback(data):
    global pose
    pose = data

def statusCallback(data):
    global status
    status = data

def getCamPos():
    rospy.Subscriber('/visp_auto_tracker/object_position', PoseStamped, poseCallback)
    rospy.Subscriber('/visp_auto_tracker/status', Int8, statusCallback)

if __name__ == "__main__":
    rospy.init_node("drive")

    rospy.loginfo("Running")
    getCamPos()

    try:
        moveCmd()
    except rospy.ROSInterruptException:
        pass
    finally:
        rospy.loginfo("Shutting Down")
        twist = Twist()
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        pub.publish(twist)