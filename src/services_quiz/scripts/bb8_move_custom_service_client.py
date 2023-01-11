#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
# from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest
# from std_srvs.srv import Empty, EmptyRequest
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('move_bb8_in_square_custom_client')
print('Waiting for service....')
rospy.wait_for_service('/move_bb8_in_square_custom')
print('connected!')
bb8_move_service = rospy.ServiceProxy(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage)
move_bb8_object = BB8CustomServiceMessageRequest()


move_bb8_object.side = 1.2
move_bb8_object.repetitions = int(2)
result = bb8_move_service(move_bb8_object)
# print('First square command sent')
print('The first square successs was : ', result)

if result.success == True:
    result.success = False
    move_bb8_object.side = 2.4
    move_bb8_object.repetitions = int(1)
    result = bb8_move_service(move_bb8_object)
    # print('Second square command sent')
    print('TThe second square success was: ', result)
