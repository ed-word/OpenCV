import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red1 = np.array([0,70,50])
    upper_red1 = np.array([5,255,255])

    #lower_red2 = np.array([170,70,50])
    #upper_red2 = np.array([180,255,255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    #mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    #mask = cv2.bitwise_or( mask1, mask2 )

    res = cv2.bitwise_and(frame,frame, mask = mask1)

    #cv2.imshow('frame',frame)
    cv2.imshow('mask',mask1)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
