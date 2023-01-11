#! /usr/bin/env python

import rospy
# you import the service message python classes generated from Empty.srv.
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
from math import pi

# you import the service message python classes
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
# generated from MyCustomServiceMessage.srv.


def my_callback(request):

    print("My_callback has been called")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    vel = Twist()
    vel2 = Twist()
    vel.linear.x = 0.0
    vel.angular.z = 1.0
    vel2.linear.x = 0.0
    vel2.angular.z = 0.0

    pub.publish(vel2)
    rospy.sleep(0.3)

    print('MOVING NOW')
    pub.publish(vel)
    sleep_time = (float(request.duration))
    print('The wait time is ', sleep_time)
    rospy.sleep(sleep_time)

    print('STOPPING NOW')
    pub.publish(vel2)
    rospy.sleep(0.2)

    answer = MyCustomServiceMessageResponse()
    answer.success = True
    return answer


rospy.init_node('move_bb8_in_square_custom_service')

# create the Service called my_service with the defined callback
my_service = rospy.Service('/move_bb8_in_square_custom',
                           MyCustomServiceMessage, my_callback)
rospy.spin()  # maintain the service open.
