#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from ros_basics_tutorials.msg import IoTSensor

def callback(data):
    '''
    Callback function for the subscriber
    Take action on the recieved data
    '''
    rospy.loginfo(rospy.get_caller_id() + 
                    " \n Sensor Data:  %d\n Sensor Name:  %s\n Temperature:  %f\n Humidity:  %f\n",
                    data.id, data.name, data.temperature, data.humidity
                    )

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("iot_sensor_topic", IoTSensor, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()