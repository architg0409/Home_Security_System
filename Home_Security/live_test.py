import cv2
import first_test
import time
import urllib.request as url
import numpy as np
import serial
import time
import threading 

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

ser = serial.Serial('COM12', 9600, timeout=0)
sampleNum=0
while(True):
    ret, img = cam.read()
##    res=url.urlopen('http://192.168.137.139:8080/shot.jpg')
##    data=np.array(bytearray(res.read()),dtype=np.uint8)
##
##    img=cv2.imdecode(data,-1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        
        
        if sampleNum>2:
            cv2.imwrite("abc.jpg", gray[y:y+h,x:x+w])
            
            
        
        cv2.imshow('frame',img)
        
    data=ser.readline().decode('utf-8')
    if data =="send":
        thread=threading.Thread(target=first_test.SendMail,args=('abc.jpg',))
        thread.start()
       
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
##    elif sampleNum>100:
##        break
cam.release()
cv2.destroyAllWindows()
