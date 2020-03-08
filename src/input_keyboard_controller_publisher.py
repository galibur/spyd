#! /usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('keyboard_controller_publisher')
pub = rospy.Publisher('user_input', String, queue_size=10)


rate = rospy.Rate(2)
msg_str = String()
msg_str = '{"keyboard":"A"}'

while not rospy.is_shutdown():

	#pub.publish(msg_str)
	rate.sleep()
