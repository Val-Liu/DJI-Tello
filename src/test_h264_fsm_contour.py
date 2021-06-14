#!/usr/bin/env python

import rospy
from h264_image_transport.msg import H264Packet
from geometry_msgs.msg import Twist
from tello_driver.msg import TelloStatus
from std_msgs.msg import Empty, UInt8
from tello_driver.msg import test
import av
import cv2
import numpy as np
import threading
import traceback
import time
import math
import apriltag

class StandaloneVideoStream(object):
    def __init__(self):
        self.cond = threading.Condition()
        self.queue = []
        self.closed = False

    def read(self, size):
        self.cond.acquire()
        try:
            if len(self.queue) == 0 and not self.closed:
                self.cond.wait(2.0)
            data = bytes()
            while 0 < len(self.queue) and len(data) + len(self.queue[0]) < size:
                data = data + self.queue[0]
                del self.queue[0]
        finally:
            self.cond.release()
        return data

    def seek(self, offset, whence):
        return -1

    def close(self):
        self.cond.acquire()
        self.queue = []
        self.closed = True
        self.cond.notifyAll()
        self.cond.release()

    def add_frame(self, buf):
        self.cond.acquire()
        self.queue.append(buf)
        self.cond.notifyAll()
        self.cond.release()


stream = StandaloneVideoStream()

global cont
cont = True

def callback(msg):
  #rospy.loginfo('frame: %d bytes' % len(msg.data))
  #if len(msg.data) > 1000:  
    stream.add_frame(msg.data)

def call(data):
  global cont
  #f.write(str(data))
  if int(data.fly_mode) == 12:
    cont = False

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
  land_sub = rospy.Subscriber('/tello/status',TelloStatus,call)
  land_pub = rospy.Publisher('/tello/land',Empty,queue_size = 1)
  rate = rospy.Rate(10)
  while cont == True:
    msg = Empty()
    land_pub.publish(msg)
    rate.sleep()

def flip():
    cmd_pub = rospy.Publisher('/tello/cmd_vel',Twist,queue_size = 10)
    rate = rospy.Rate(10)
    count = 20
    while not rospy.is_shutdown():
      if count >0:
        msg = Twist()
        msg.linear.y = -0.3
        cmd_pub.publish(msg)
        rate.sleep()
        count -= 1
      else:
        cmd_pub.publish(Twist())
        rate.sleep()
        break
      
    
def round():
    round_pub = rospy.Publisher('/tello/cmd_vel',Twist,queue_size = 10)
    rate = rospy.Rate(10)
    count = 20
    while not rospy.is_shutdown():
      if count>0:
        msg = Twist()
        msg.angular.z = 0.6
        round_pub.publish(msg)
        rate.sleep()
        count -= 1
      else:
        round_pub.publish(Twist())
        rate.sleep()
        break
def back():
    forward_pub = rospy.Publisher('/tello/cmd_vel',Twist,queue_size = 10)
    cmd_flip = rospy.Publisher('/tello/flip',UInt8,queue_size = 10)
    rate = rospy.Rate(10)
    count = 50
    while not rospy.is_shutdown():
      if count>0 and count != 1:
        msg = Twist()
        msg.linear.x = 0.3
        forward_pub.publish(msg)
        rate.sleep()
        count -= 1
      elif count == 1:
        cmd_flip.publish(0)
        rate.sleep()
        time.sleep(3)
        count -= 1
      else:
        msg = Twist()
        msg.linear.x = 0.0
        rospy.loginfo(msg)
        forward_pub.publish(msg)
        rate.sleep()
        break


def findMask(img):
  lr0 = np.array([0,150,0])
  ur0 = np.array([5,255,255])
  lr1 = np.array([175,150,0])
  ur1 = np.array([180,255,255])
  #lb = np.array([112,170,0])
  #ub = np.array([128,255,255])
  rm0 = cv2.inRange(img, lr0, ur0)
  rm1 = cv2.inRange(img, lr1, ur1)
  #bm = cv2.inRange(img, lb, ub)
  rm = cv2.bitwise_or(rm0, rm1)
  #m = cv2.bitwise_or(rm, bm)
  return rm

def findMask1(img):
  lb = np.array([100,30,0])
  ub = np.array([140,255,255])
  bm = cv2.inRange(img, lb, ub)
  return bm

def main():
    old_center = [0,0]
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    out = cv2.VideoWriter('test_contour.avi', fourcc, 30.0, (1920, 720))
    #rospy.init_node('h264_listener')
    rospy.Subscriber("/tello/image_raw/h264", H264Packet, callback)
    pub = rospy.Publisher('/selfDefined', test, queue_size = 1)
    container = av.open(stream)
    rospy.loginfo('main: opened')
    detector = apriltag.Detector()
    frame_skip = 300
    t = 0
    thr = 0.32
    for frame in container.decode(video=0):
        if 0 < frame_skip:
          frame_skip -= 1
          continue
        start_time = time.time()
        image = cv2.cvtColor(np.array(frame.to_image()), cv2.COLOR_RGB2BGR)
        img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        blurred_img = cv2.GaussianBlur(image, (13, 13), 0)
        result = detector.detect(img)
        #print(result[0].tag_id)
        if len(result)!=0:
          print(result[0].tag_id)
          if result[0].tag_id == 0:
            flip()
          elif result[0].tag_id == 1:
            round()
          elif result[0].tag_id == 2:
            back()
            time.sleep(3)
            L()
          else:
            continue

        '''hsv_img = cv2.cvtColor(blurred_img.copy(), cv2.COLOR_BGR2HSV)
        if t == 1:
          red_mask = findMask(hsv_img)
          thr = 0.32
        elif t == 0:
          red_mask = findMask1(hsv_img)
          thr = 0.3
        (c_i, c_c, c_h) = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        show_image = cv2.cvtColor(c_i, cv2.COLOR_GRAY2BGR)
        cv2.drawContours(show_image, c_c, 0, (0,0,255), -1)
        if(len(c_c) == 0):
          pub.publish(test([0,0,0]))
          continue
        out_max_contours = max(c_c, key = cv2.contourArea)
        rect = cv2.minAreaRect(out_max_contours)
        rect_width, rect_height = rect[1]
        if(rect_width*rect_height < 0.2*960*720.0):
          pub.publish(test([0,0,0]))
          continue
        #avg_x = []
        #avg_y = []
        #for c in out_max_contours:
        #    avg_x.append(c[0][0])
        #    avg_y.append(c[0][1])
        ce_x = rect[0][0] + 1/2*rect_width
        ce_y = rect[0][1] + 1/2*rect_height
        if old_center[0] == 0 and old_center[1] == 0:
          old_center = [int(ce_x),int(ce_y)]
          pub.publish(test([int(old_center[0]),int(old_center[1]),1]))
        else:
          #print(math.sqrt( (int(mean_y) - old_center[0])**2 + (int(mean_x) - old_center[1])**2 ))
          cv2.putText(show_image, str(rect_width*rect_height / (960*720.0)), (10,40),5 ,2, 255)
          if rect_width*rect_height >= 960*720*thr:
            pub.publish(test([old_center[0],old_center[1],-1]))
            print(">= 100")
            temp = time.time()
            while time.time() - temp < 3.1:
              pass
            t = 1
          else:
            old_center = [int(ce_x),int(ce_y)]
            pub.publish(test([int(old_center[0]),int(old_center[1]),1]))
        
        out.write(np.concatenate((blurred_img, show_image), axis=1))
        cv2.imshow('result', np.concatenate((blurred_img, show_image), axis=1))
        cv2.waitKey(1)'''
        if frame.time_base < 1.0/60:
          time_base = 1.0/60
        else:
          time_base = frame.time_base
        frame_skip = int((time.time() - start_time)/time_base)

if __name__ == '__main__':
    try:
      TO()
      main()
    except BaseException:
        traceback.print_exc()
    finally:
        stream.close()
        cv2.destroyAllWindows()
