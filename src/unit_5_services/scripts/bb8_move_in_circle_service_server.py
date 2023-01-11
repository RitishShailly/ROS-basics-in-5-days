#! /usr/bin/env python

import rospy
# you import the service message python classes generated from Empty.srv.
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
from math import pi


def my_callback(request):

    print("My_callback has been called")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    vel = Twist()
    vel2 = Twist()
    vel.linear.x = 1.0
    vel.angular.z = 1.0
    vel2.linear.x = 0.0
    vel2.angular.z = 0.0
    pub.publish(vel2)
    rospy.sleep(0.5)
    print('MOVING NOW')
    pub.publish(vel)
    rospy.sleep(pi*2.1)

    print('STOPPING NOW')
    pub.publish(vel2)
    rospy.sleep(pi/4)
    # print(MyServiceResponse(len(request.words.split())))
    return EmptyResponse()  # the service Response class, in this case EmptyResponse
    # return MyServiceResponse(len(request.words.split()))


rospy.init_node('service_server')

# create the Service called my_service with the defined callback
my_service = rospy.Service('/move_bb8_in_circle', Empty, my_callback)
rospy.spin()  # maintain the service open.
