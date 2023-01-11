#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')
pub1 = rospy.Publisher('/counter', Int32, queue_size=1)
pub2 = rospy.Publisher('/adder', Int32, queue_size=1)
rate = rospy.Rate(2)
count = Int32()
count.data = 0
adder = Int32()
adder.data = 0

while not rospy.is_shutdown():
    pub1.publish(count)
    pub2.publish(adder)
    count.data += 1
    adder.data = adder.data + count.data
    rate.sleep()
