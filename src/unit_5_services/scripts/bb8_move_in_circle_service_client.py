#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
# from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest
from std_srvs.srv import Empty, EmptyRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('bb8_move_in_circle_service_client')
# Wait for the service client /trajectory_by_name to be running
print('Waiting for service....')
rospy.wait_for_service('/move_bb8_in_circle')
print('connected!')
# Create the connection to the service
bb8_move_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
# Create an object of type TrajByNameRequest
move_bb8_object = EmptyRequest()
# Fill the variable traj_name of this object with the desired value
# move_bb8_object.traj_name = "release_food"
# print('sending message')
# Send through the connection the name of the trajectory to be executed by the robot
result = bb8_move_service(move_bb8_object)
print('Sent')
# Print the result given by the service called

print('The command sent was : ', result)
