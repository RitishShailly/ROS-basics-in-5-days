#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

print(LaserScan().ranges)

range_forward = float("inf")
range_left = float("inf")
range_right = float("inf")

alpha = 1

rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(100)
vel = Twist()


def callback(msg):
    range_forward = float(msg.ranges[359])
    range_left = float(msg.ranges[719])
    range_right = float(msg.ranges[0])
    if range_forward >= 1.0:
        vel.linear.x = alpha * 1
        vel.angular.z = 0.0
    if range_forward < 1.0:
        vel.linear.x = 0
        vel.angular.z = alpha
    if range_left < 1.0:
        vel.linear.x = 0.0
        vel.angular.z = -alpha
    if range_right < 1.0:
        vel.linear.x = 0.0
        vel.angular.z = alpha
    pub.publish(vel)
    rate.sleep()


sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rospy.spin()
