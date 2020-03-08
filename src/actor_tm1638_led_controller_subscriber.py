#! /usr/bin/env python

import time
from time import sleep
from rpi_TM1638 import TMBoards

import rospy
from std_msgs.msg import String

actor_id = 3

DIO = 19
CLK = 13
STB = 26
TM = TMBoards(DIO, CLK, STB, 0)
TM.clearDisplay()

while True:
	TM.leds[6] = True
	sleep(0.5)

for i in range(8):
	#TM.leds[i] = False
	''

def callback(msg):
	
	print("# actor_tm1638_led_controller_subscriber: ")
	print(msg.data)
	#TM.leds[1] = True
		

rospy.init_node('actor_tm1638_led_controller_subscriber')
sub = rospy.Subscriber('/tm1638_led_command', String, callback)


rospy.spin()


