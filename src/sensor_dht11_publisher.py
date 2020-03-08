#!/usr/bin/python

import sys
import rospy
import time
from std_msgs.msg import String

import Adafruit_DHT

pin = 5
sensor = 11
sensor_id = 3

rospy.init_node('sensor_dht11_publisher_' + str(sensor_id))
pub = rospy.Publisher('system', String, queue_size=10)

rate = rospy.Rate(10)
msg_str = String()

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
while not rospy.is_shutdown():

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		#print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
	    	msg_str = '{"dht11_temperature_' + str(sensor_id) + '":' + str(temperature) + '}'
		pub.publish(msg_str)
	    	msg_str = '{"dht11_humidity_' + str(sensor_id) + '":' + str(humidity) + '}'
		pub.publish(msg_str)
	else:
	    	#print('Failed to get reading. Try again!')
		''

	time.sleep(10)
sys.exit(1)
