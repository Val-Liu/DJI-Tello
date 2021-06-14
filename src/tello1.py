#!/usr/bin/env python
import rospy
import roslib
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty, UInt8
from tello_driver.msg import TelloStatus
from time import sleep

global cont
cont = True

f = open("107753028.txt", 'w')

f.write("-----------\n")

def TO():
	takeoff_pub = rospy.Publisher('/tello/takeoff',Empty,queue_size = 1)
	rospy.init_node('turtlesim_pub',anonymous = True)
	rate = rospy.Rate(10)
	msg = Empty()
	rospy.loginfo(msg)
	takeoff_pub.publish(msg)
	rate.sleep()

def L():
	global cont
	land_sub = rospy.Subscriber('/tello/status',TelloStatus,callback)
	land_pub = rospy.Publisher('/tello/land',Empty,queue_size = 1)
	rate = rospy.Rate(10)
	while cont == True:
		msg = Empty()
		land_pub.publish(msg)
		rate.sleep()

def cmd():
	cmd_pub = rospy.Publisher('/tello/cmd_vel',Twist,queue_size = 10)
    cmd_flip = rospy.Publisher('/tello/flip',UInt8,queue_size = 10)
	rate = rospy.Rate(10)
	count = 60
	while not rospy.is_shutdown():
		if count>2:
			msg = Twist()
			msg.linear.x = 0.43
			msg.angular.z = 0.36
			rospy.loginfo(msg)
			cmd_pub.publish(msg)
			rate.sleep()
			count -= 1
		elif count == 2:
			msg = Twist()
			msg.linear.x = 0.0
			rospy.loginfo(msg)
			cmd_pub.publish(msg)
			rate.sleep()
			count-=1	
		elif count == 1:
			
			cmd_flip.publish(1)
			rate.sleep()
				
			count -= 1
		else:
			break
	print("end loop")
def forward(): 
	forward_pub = rospy.Publisher('/tello/cmd_vel',Twist,queue_size = 10)
	rate = rospy.Rate(10)
	count = 50
	while not rospy.is_shutdown():
		if count>0:
			msg = Twist()
			msg.linear.x = 0.4
			rospy.loginfo(msg)
			forward_pub.publish(msg)
			rate.sleep()
			count -= 1
		else:
			msg = Twist()
			msg.linear.x = 0.0
			rospy.loginfo(msg)
			forward_pub.publish(msg)
			rate.sleep()
			break

def left():
	left_pub = rospy.Publisher('/tello/cmd_vel',Twist,queue_size = 10)
	rate = rospy.Rate(10)
	count = 5
	while not rospy.is_shutdown():
		if count>0:
			msg = Twist()
			msg.angular.z = 0.4
			rospy.loginfo(msg)
			left_pub.publish(msg)
			rate.sleep()
			count -= 1
		else:
			break

def callback(data):
	global cont
	f.write(str(data))
	if int(data.fly_mode) == 12:
		cont = False

if __name__ == '__main__':
	try:
		'''rospy.init_node('turtlesim_pub',anonymous = True)
		print(rospy.get_time())
		sleep(3)
		print(rospy.get_time())'''
		TO()
		sleep(5)
		forward()
		sleep(3)
		left()
		sleep(3)
		cmd()
		sleep(3)
		L()
	except rospy.ROSInterruptException:
		print(e)
	finally:
		sys.exit(0)