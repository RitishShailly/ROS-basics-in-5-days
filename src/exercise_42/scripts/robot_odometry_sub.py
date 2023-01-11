#! /usr/bin/env python
 
import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    print('\n-----THIS IS WHAT I READ------\n')
    print(msg.pose)
    print('-----THIS MARKS THE END OF MESSAGE------\n')


rospy.init_node('odometry_subscriber')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
