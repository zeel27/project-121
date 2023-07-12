import cv2
import time
import numpy as np

cap=cv2.VideoCapture(0)
image=cv2.imread("imagep121.jpg")

while True: 
    ret,img=cap.read() 
#img=cv2.resize(img,(640,480))
#image=cv2.resize(image,(640,480))
    ublack=np.array([104,153,70])
    lblack=np.array([30,30,0])
    mask=cv2.inRange(img,lblack,ublack)
    res=cv2.bitwise_and(img,img,mask=mask)
    f=img-res
    f=np.where(f==0,image,f)
   
    cv2.imshow("magic",img)
    cv2.imshow("mask",f) 
    cv2.waitKey(0) 

cap.release()
cv2.destroyAllWindows()  