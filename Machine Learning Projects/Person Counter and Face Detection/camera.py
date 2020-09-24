# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:37:26 2020

@author: lenovo

"""


import cv2
from mtcnn import mtcnn

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()
        
    def get_frame(self):
            detector =mtcnn.MTCNN()
            
           #extracting frames
            ret, frame = self.video.read()
            
     #       if ret == True : 
        
    
            faces = [i['box'] for i in detector.detect_faces(frame)]
            
            
            for (a,b,c,d) in faces:
                cv2.rectangle(frame, (a,b), (a+c, b+d), ( 0, 255,0), 1)
                break
            cv2.putText(frame,str("faces : " + str(len(faces)) ),(2,100), cv2.FONT_HERSHEY_SIMPLEX, 1,( 255, 0 ,0),2)
    
            
            # encode OpenCV raw frame to jpg and displaying it
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        
"""

# import the necessary packages
import cv2
# defining face detector
face_cascade=cv2.CascadeClassifier("C://Users//lenovo//Anaconda3//Lib//site-packages//cv2//data//haarcascade_frontalface_default.xml")
ds_factor=0.6
class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()
        
    def get_frame(self):
           #extracting frames
            ret, frame = self.video.read()
            frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)                    
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face_rects=face_cascade.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in face_rects:
             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
             break
            # encode OpenCV raw frame to jpg and displaying it
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

"""
