#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
# from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest
from std_srvs.srv import Empty, EmptyRequest
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('move_bb8_in_circle_custom_client')
# Wait for the service client /trajectory_by_name to be running
print('Waiting for service....')
rospy.wait_for_service('/move_bb8_in_circle_custom')
print('connected!')
# Create the connection to the service
bb8_move_service = rospy.ServiceProxy(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage)
# Create an object of type TrajByNameRequest
move_bb8_object = MyCustomServiceMessageRequest()
moving_time = input("For how long do you want the robot to move? : ")
move_bb8_object.duration = int(moving_time)
# print('sending message')
# Send through the connection the name of the trajectory to be executed by the robot
result = bb8_move_service(move_bb8_object)
print('Sent')
# Print the result given by the service called

print('The command sent was : ', result)
