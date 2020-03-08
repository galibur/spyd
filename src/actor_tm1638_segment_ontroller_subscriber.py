#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
# in use: 23,24,25



import rospy
from std_msgs.msg import String

def callback(msg):
	
	print "# led_controller_subscriber: "
	print msg.data
	#print msg.data

	GPIO.output(23, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(23, GPIO.LOW)
	#time.sleep(0.5)
	#GPIO.output(24, GPIO.HIGH)
	#time.sleep(0.5)
	#GPIO.output(24, GPIO.LOW)
	#time.sleep(0.5)
	#GPIO.output(25, GPIO.HIGH)
	#time.sleep(0.5)
	#GPIO.output(25, GPIO.LOW)
	#time.sleep(0.5)
	#GPIO.output(18, GPIO.HIGH)
	#time.sleep(0.5)
	#GPIO.output(18, GPIO.LOW)
	#time.sleep(0.5)

rospy.init_node('led_controller_subscriber')
sub = rospy.Subscriber('/user_input', String, callback)


rospy.spin()


