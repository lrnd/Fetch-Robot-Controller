#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped


def printdata(data):
    rospy.loginfo('data x:, %f', data.pose.position.x)
    rospy.loginfo('data y:, %f', data.pose.position.y)
    rospy.loginfo('data z:, %f', data.pose.position.z)


def getpose():
    rospy.init_node('results')
    rospy.Subscriber('/visp_auto_tracker/object_position', PoseStamped, printdata)
    rospy.spin()

if __name__ == "__main__":
    getpose()







