#!/usr/bin/env python

from time import sleep
import rospy
from std_msgs.msg import String

board_id = 3

rospy.init_node('tm1638_led_test_publisher')
pub = rospy.Publisher('tm1638_commands', String, queue_size=10)

led_id = 0

while not rospy.is_shutdown():
	
	
	msg = '{"board_id":' + str(board_id) + ',"function":"led","id":' + str(led_id) + ',"status":1}'
	print(msg)
	pub.publish(msg)
	sleep(0.2)
	msg = '{"board_id":' + str(board_id) + ',"function":"led","id":' + str(led_id) + ',"status":0}'
	print(msg)
	pub.publish(msg)

	
	if led_id >= 7:
		led_id = 0
	else:
		led_id += 1


	sleep(0.2)
