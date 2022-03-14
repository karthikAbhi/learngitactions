#!/usr/bin/env python3

from random import random
from time import ctime, time

import rospy
from ros_basics_tutorials.msg import IoTSensor
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('iot_sensor_topic', IoTSensor, queue_size = 10)
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # Freq 
    i = 0
    while not rospy.is_shutdown():
        iot_sensor = IoTSensor()
        iot_sensor.id = i
        iot_sensor.name = "iot_parking_01"
        iot_sensor.temperature = 24.35 + random()*2
        iot_sensor.humidity = 33.5 + random()*2
        i = i + 1

        # hello_str = ctime(time())
        rospy.loginfo(iot_sensor)
        pub.publish(iot_sensor)
        rate.sleep() # Based on Freq (1/rate)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
