#!/usr/bin/env python

from time import sleep
from rpi_TM1638 import TMBoards

import json
import rospy
from std_msgs.msg import String

rospy.init_node('io_tm1638_publisher_subscriber')
pub = rospy.Publisher('user_input', String, queue_size=10)

sensor_id = 3
last_msg = False

DIO = 19
CLK = 13
STB = 26

TM = TMBoards(DIO, CLK, STB, 0)

TM.clearDisplay()

switchStatus = [0,0,0,0,0,0,0,0]

last_msg = "-1"

def tm1638_subscriber_callback(msg):
	global last_msg
	if msg.data != last_msg:
		print( str(msg))
	
		obj = json.loads(msg.data)

		if obj['board_id'] == sensor_id:
			
			if obj['function'] == "led":
				if obj['id'] >= 0 and obj['id'] < 8:
					if obj['status'] == 0:
						TM.leds[obj['id']] = False
						print(str(obj['id']) + ", " + str(obj['status']))
					elif obj['status'] == 1:
						TM.leds[obj['id']] = True

			elif obj['function'] == "segment":
				TM.segments[obj['id']] = str(obj['status'])
			

		last_msg = msg.data


while not rospy.is_shutdown():
	for i in range(8):
		is_new_status = False
		if TM.switches[i] and switchStatus[i] != 1:
				switchStatus[i] = 1
				is_new_status = True
		elif not TM.switches[i] and switchStatus[i] != 0:
				switchStatus[i] = 0
				is_new_status = True

		if is_new_status:
			msg_str = '{"user_input":"tm1638_buttons_' + str(sensor_id) + '","' + str(i) + '":' + str(switchStatus[i]) + '}'
			print(msg_str)
			pub.publish(msg_str)

	sub = rospy.Subscriber('/tm1638_commands', String, tm1638_subscriber_callback)
	sleep(0.02)
