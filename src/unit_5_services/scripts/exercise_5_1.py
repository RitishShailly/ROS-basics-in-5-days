#! /usr/bin/env python

import rospy
# Import the service message used by the service /iri_wam_reproduce_trajectory
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys
import rospkg

# Initialise a ROS node with the name service_client
print('Initialising node')
rospy.init_node('service_execute_trajectory_client')
# Wait for the service client /iri_wam_reproduce_trajectory to be running
print('Waiting for service')
rospy.wait_for_service('/execute_trajectory')


rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + \
    "/config/release_food.txt"
print('\n\n\n\------The path is: ', traj, '------\n\n\n')

# Create the connection to the service
print('Connected to service')
exec_traj_service_client = rospy.ServiceProxy(
    '/execute_trajectory', ExecTraj)

print('creating ExecTrajRequest object')
exec_traj_object = ExecTrajRequest()
# Fill the variable traj_name of this object with the desired value
print('making result variable')
exec_traj_object.file = traj
# Send through the connection the name of the trajectory to be executed by the robot
print('sending result')
result = exec_traj_service_client(exec_traj_object)
print('sent')
# Print the result given by the service called
print(result)
