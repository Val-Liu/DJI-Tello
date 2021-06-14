#!/usr/bin/env python

import rospy
import roslib
import sys
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty, UInt8
from tello_driver.msg import TelloStatus, test
from time import sleep

global target
target = (-1,-1,1)

global center 
center = (470, 350)

global check
check = False

global canLand
canLand = False

global rec_time
rec_time = 0

def callback(data):
  global target
  global rec_time
  rec_time = rospy.get_time()
  target = data.l1

def ts_callback(data):
  global canLand
  if data.fly_mode == 12:
    canLand = True

def cmd():
  #The queue_size argument is New in ROS hydro and limits the amount of queued messages if any subscriber is not receiving them fast enough
  rospy.init_node('h264_pub', anonymous=True)
  self_pub = rospy.Subscriber('/selfDefined', test, callback)
  cmd_pub = rospy.Publisher('/tello/cmd_vel', Twist, queue_size = 10)
  rate = rospy.Rate(10)

  count = 0
  global target
  global center
  global check
  global rec_time

  while target[0] == -1 and target[1] == -1:
    pass 

  while not rospy.is_shutdown():
    dx = target[0] - center[0]
    dy = target[1] - center[1]

    if target[2] == -1:
      msg = Twist()
      msg.linear.x = 0.2
      msg.linear.z = -0.2
      cmd_pub.publish(msg)
      rate.sleep()
      sleep(2)
      msg = Twist()
      msg.linear.x = 0.3 
      cmd_pub.publish(msg)
      rate.sleep()
      sleep(3)
      msg = Twist()
      cmd_pub.publish(msg)
      rate.sleep()
      break  
    elif rospy.get_time() - rec_time > 1.0:
      msg = Twist()
      cmd_pub.publish(msg)
      rate.sleep()
    else:
      if check == False:
        if abs(dx) < 24 and abs(dy) < 28:
          check = True
          msg = Twist()
          msg.linear.x = 0.2
          cmd_pub.publish(msg)
          rate.sleep()
        else:
          msg = Twist()
          if dx != 0:
            msg.linear.y = -dx / abs(dx) * 0.1

          if dy != 0:
            msg.linear.z = -dy / abs(dy) * 0.2
         
          cmd_pub.publish(msg)
          rate.sleep()
      else:    
        if abs(dx) >= 60 or abs(dy) >= 30:  
          msg = Twist()
          if abs(dx) >= 60:
            msg.linear.y = -dx / abs(dx) * 0.1
          if abs(dy) >= 30:
            msg.linear.z = -dy / abs(dy) * 0.2
          cmd_pub.publish(msg)
          rate.sleep()
        else:
          msg = Twist()
          msg.linear.x = 0.2
          cmd_pub.publish(msg)
          rate.sleep()
 
  
  msg = Twist()
  cmd_pub.publish(msg)
  rate.sleep()  
  print("end loop")

def L():
  global canLand
  land_sub = rospy.Subscriber('/tello/status', TelloStatus, ts_callback)
  land_pub = rospy.Publisher('/tello/land', Empty, queue_size = 1)
  rate = rospy.Rate(10)
  
  while canLand is not True:
    msg = Empty()
    land_pub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
    cmd()
    sleep(3)
    sys.exit(0)
