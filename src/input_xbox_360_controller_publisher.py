#!/usr/bin/env python

from __future__ import print_function
import signal
import sys
import xbox
import rospy
from std_msgs.msg import String

rospy.init_node('xbox_360_controller_publisher')
pub = rospy.Publisher('user_input', String, queue_size=10)

rate = rospy.Rate(2)
msg_str = String()

joy = xbox.Joystick()

class Controller():
	def __init__(self):

		self.pub = pub
		self.mgs = False

		self.joy = joy
		self.online = self.check_connection()
		self.a = 0
		self.b = 0
		self.x = 0
		self.y = 0
		
		self.up = 0
		self.down = 0
		self.left = 0
		self.right = 0

		self.leftX = 0
		self.leftY = 0

		self.rightX = 0
		self.rightY = 0

		self.back = 0
		self.guide = 0
		self.start = 0

		self.leftThumbstick = 0
		self.rightThumbstick = 0

		self.leftBumper = 0	
		self.rightBumper = 0	

		self.leftTrigger = 0
		self.rightTrigger = 0

	def check_connection(self):
	        if self.joy.connected():
			self.online = True
		else:
			self.online = False


	def make_msg(self,key, val):
		self.msg = '{"user_input":"xbox", "key":"' + str(key) + '", "val":' + str(val) + '}'
		#print(self.msg)
		self.publish_message()


	def publish_message(self):
		self.pub.publish(self.msg)	


	def read(self):

		self.check_connection()

		if self.online:
			if self.joy.A() and self.a != 1:	
				self.a = 1
				self.make_msg("A", 1)
			elif not self.joy.A() and self.a != 0:	
				self.a = 0
				self.make_msg("A", 0)

			if self.joy.B() and self.b != 1:	
				self.b = 1
				self.make_msg("B", 1)
			elif not self.joy.B() and self.b != 0:	
				self.b = 0
				self.make_msg("B", 0)

			if self.joy.X() and self.x != 1:	
				self.x = 1
				self.make_msg("X", 1)
			elif not self.joy.X() and self.x != 0:	
				self.x = 0
				self.make_msg("X", 0)

			if self.joy.Y() and self.y != 1:	
				self.y = 1
				self.make_msg("Y", 1)
			elif not self.joy.Y() and self.y != 0:	
				self.y = 0
				self.make_msg("Y", 0)

			if self.joy.leftX() != self.leftX:
				self.leftX = self.joy.leftX()
				self.make_msg("LEFT_X", self.leftX)

			if self.joy.leftY() != self.leftY:
				self.leftY = self.joy.leftY()
				self.make_msg("LEFT_Y", self.leftY)

			if self.joy.rightX() != self.rightX:
				self.rightX = self.joy.rightX()
				self.make_msg("RIGHT_X", self.rightX)

			if self.joy.rightY() != self.rightY:
				self.rightY = self.joy.rightY()
				self.make_msg("RIGHT_Y", self.rightY)

			if self.joy.dpadDown() != self.down:
				self.down = self.joy.dpadDown()
				self.make_msg("DOWN", self.down)

			if self.joy.dpadLeft() != self.left:
				self.left = self.joy.dpadLeft()
				self.make_msg("LEFT", self.left)

			if self.joy.dpadRight() != self.right:
				self.right = self.joy.dpadRight()
				self.make_msg("RIGHTP", self.right)

			if self.joy.dpadUp() != self.up:
				self.up = self.joy.dpadUp()
				self.make_msg("UP", self.up)

			if self.joy.Back() != self.back:
				self.back = self.joy.Back()
				self.make_msg("BACK", self.back)

			if self.joy.Guide() != self.guide:
				self.guide = self.joy.Guide()
				self.make_msg("GUIDE", self.guide)

			if self.joy.Start() != self.start:
				self.start = self.joy.Start()
				self.make_msg("START", self.start)

			if self.joy.leftThumbstick() != self.leftThumbstick:
				self.leftThumbstick = self.joy.leftThumbstick()
				self.make_msg("LEFT_THUMBSTICK", self.leftThumbstick)

			if self.joy.rightThumbstick() != self.rightThumbstick:
				self.rightThumbstick = self.joy.rightThumbstick()
				self.make_msg("RIGHT_THUMBSTICK", self.rightThumbstick)

			if self.joy.leftTrigger() != self.leftTrigger:
				self.leftTrigger = self.joy.leftTrigger()
				self.make_msg("LEFT_TRIGGER", self.leftTrigger)

			if self.joy.rightTrigger() != self.rightTrigger:
				self.rightTrigger = self.joy.rightTrigger()
				self.make_msg("RIGHT_TRIGGER", self.rightTrigger)

			if self.joy.leftBumper() != self.leftBumper:
				self.leftBumper = self.joy.leftBumper()
				self.make_msg("LEFT_BUMPER", self.leftBumper)

			if self.joy.rightBumper() != self.rightBumper:
				self.rightBumper = self.joy.rightBumper()
				self.make_msg("RIGHT_BUMPER", self.rightBumper)


con = Controller()

def main():
    	while not rospy.is_shutdown():
		#while not con.joy.Back():
		#while True:
		con.read()

	con.joy.close()


def clean_close(signal, frame):
	con.joy.close()
	print("clean exit")	
	sys.exit(0)

signal.signal(signal.SIGINT, clean_close)

if __name__ == "__main__":
    	main()
