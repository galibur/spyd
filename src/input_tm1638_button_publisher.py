#!/usr/bin/env python

from time import sleep
from rpi_TM1638 import TMBoards

import rospy
from std_msgs.msg import String

rospy.init_node('input_tm1638_button_publisher')
pub = rospy.Publisher('user_input', String, queue_size=10)

sensor_id = 3

# (one TM1638 board connected to GPIO19 for dataIO, GPIO13 for Clock, and GPIO26 for the STB)
DIO = 19
CLK = 13
STB = 26
# STB = 6, 26   # in case you have two TM1638 boards, connected to GPIO06 and GPIO26

# instanciante my TMboards
TM = TMBoards(DIO, CLK, STB, 0)

#TM.clearDisplay()

switchStatus = [0,0,0,0,0,0,0,0]

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
			msg_str = '{"user_input":"tmp1638_buttons_' + str(sensor_id) + '","' + str(i) + '":' + str(switchStatus[i]) + '}'
			#print(msg_str)
			pub.publish(msg_str)


	
'''
def switchLed(led_id, led_status):
	if led_status == 1:
		TM.leds[led_id] = True
	else:
		TM.leds[led_id] = False
'''



# some LEDs manipulation
#TM.leds[0] = True       # turn on led 0 (1st led of the 1st board)


#TM.segments[1] = '0'        # display '0' on the display 1 (2nd 7-segment display of the 1st board)
#TM.segments[4] = '98.76'     # display '9876' on the 7-segment display number 4, 5, 6 and 7 (the point is on segment 5)
#TM.segments[3, 1] = True     # turn on the segment #1 of the 7-segment number 3

#TM.segments[8] = '01234567'


# while True:
# 	TM.segments[0] = 'OK  ' if TM.switches[0] else 'OK  '
# 	TM.segments[4] = 'OK  ' if TM.switches[1] else 'OK  '
# 	sleep(0.01)
