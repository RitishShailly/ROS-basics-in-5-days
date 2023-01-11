#! /usr/bin/env python

import rospy
# you import the service message python classes generated from Empty.srv.
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
# from math import pi


def my_callback(request):

    print("My_callback has been called")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    num_side = 4
    reps = request.repetitions
    side = request.side

    vel_lin = Twist()
    vel_lin.linear.x = 1.0
    vel_lin.angular.z = 0.0

    vel_rot = Twist()
    vel_rot.linear.x = 0.0
    vel_rot.angular.z = 1

    vel_stop = Twist()
    vel_stop.linear.x = 0.0
    vel_stop.angular.z = 0.0

    # Settinhg up times
    lin_time = 1.05 * side/vel_lin.linear.x
    rot_time = 2.1
    sleep_time = 0.5

    #
    pub.publish(vel_stop)
    rospy.sleep(sleep_time)

    for i in range(reps):
        for y in range(num_side):
            print('Linear')
            pub.publish(vel_lin)
            rospy.sleep(lin_time)

            print('Rotating')
            pub.publish(vel_rot)
            rospy.sleep(rot_time)

            print('Stopping')
            pub.publish(vel_stop)
            rospy.sleep(sleep_time)

    print('DONE! \n')

    answer = BB8CustomServiceMessageResponse()
    answer.success = True
    return answer


rospy.init_node('move_bb8_in_square_custom_service')

# create the Service called my_service with the defined callback
my_service = rospy.Service('/move_bb8_in_square_custom',
                           BB8CustomServiceMessage, my_callback)
rospy.spin()  # maintain the service open.
