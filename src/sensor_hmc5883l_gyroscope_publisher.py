#!/usr/bin/python
import smbus
import sys
import time
import math
import rospy
from std_msgs.msg import String

bus = smbus.SMBus(1)
address = 0x1e

sensor_id = 3
rospy.init_node('sensor_hmc5883l_gyroscope_publisher_' + str(sensor_id))
pub = rospy.Publisher('system', String, queue_size=10)


def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def write_byte(adr, value):
    bus.write_byte_data(address, adr, value)

while not rospy.is_shutdown():

	write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
	write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
	write_byte(2, 0b00000000) # Continuous sampling

	scale = 0.92

	x_out = read_word_2c(3) * scale
	y_out = read_word_2c(7) * scale
	z_out = read_word_2c(5) * scale

	bearing  = math.atan2(y_out, x_out) 
	if (bearing < 0):
   		bearing += 2 * math.pi

	#print "Bearing: ", math.degrees(bearing)
	#print("x_out: " + str(x_out))
	#print("Y_out: " + str(y_out))
	#print("Z_out: " + str(z_out))

	msg_str = '{"hmc5883l_gyro":' + str(sensor_id) + ',"bearing":' + str(bearing) + ',"x":' + str(x_out) + ',"y":' + str(y_out) + ',"z":' + str(z_out) + '}'
	
	pub.publish(msg_str)

	time.sleep(1)
sys.exit(1)
