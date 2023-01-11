#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pi

rospy.init_node('circle_robot_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
vel = Twist()
vel2 = Twist()
vel.linear.x = 1.0
vel.angular.z = 1.0
vel2.linear.x = 0.0
vel2.angular.z = 0.0

while not rospy.is_shutdown():
    print('MOVING NOW')
    pub.publish(vel)
    rospy.sleep(pi*2.1)
    print('STOPPING NOW')
    pub.publish(vel2)
    rospy.sleep(pi/4)
    rate.sleep()
