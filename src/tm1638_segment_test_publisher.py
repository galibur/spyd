#!/usr/bin/env python

from time import sleep
import rospy
from std_msgs.msg import String

board_id = 3

rospy.init_node('tm1638_led_test_publisher')
pub = rospy.Publisher('tm1638_commands', String, queue_size=10)

status = 9

while not rospy.is_shutdown():
	
	
	msg = '{"board_id":' + str(board_id) + ',"function":"segment","id":3,"status":' + str(status) + '}'
	print(msg)
	pub.publish(msg)

	if status > 0:
		status -= 1
	else:
		status = 9
	sleep(1)
