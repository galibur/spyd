#!/usr/bin/env python

from __future__ import print_function
from inputs import get_gamepad
import rospy
from std_msgs.msg import String

rospy.init_node('gamepad_controller_publisher2')
pub = rospy.Publisher('user_input', String, queue_size=10)

rate = rospy.Rate(2)
msg_str = String()

def main():
    while not rospy.is_shutdown():
        events = get_gamepad()
        for event in events:
		evt = False
		if event.ev_type == "Key":
        	    	#print(event.ev_type, event.code, event.state)
			evt = event
		elif event.ev_type == "Absolute":
            		#print(event.ev_type, event.code, event.state)
			#''
			if event.code == "ABS_HAT0X":
				evt = event
        	    		#print(event.ev_type, event.code, event.state)
			elif event.code == "ABS_HAT0Y":
				evt = event
        	    		#print(event.ev_type, event.code, event.state)

		elif event.ev_type == "Sync":
            		#print(event.ev_type, event.code, event.state)
			''
		elif event.ev_type != "Misc":
            		#print(event.ev_type, event.code, event.state)
			''
		
		if evt:
			msg_str = '{"user_input":"gamepad","' + evt.code + '": ' + str(evt.state) + '}'
			pub.publish(msg_str)	
		

if __name__ == "__main__":
    main()

