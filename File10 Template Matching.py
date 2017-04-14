import cv2
import numpy as np

img_rgb = cv2.imread('template-main.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.jpg',0)
width, height = template.shape[::-1]

template1 = cv2.imread('template1.jpg',0)
width, height = template.shape[::-1]


res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc1 = np.where( res >= threshold)

res = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc2 = np.where( res >= threshold)



for pt in zip(*loc1[::-1]):
    cv2.rectangle( img_rgb, pt, (pt[0] + width, pt[1] + height), (0,255,255), 2)

for pt in zip(*loc2[::-1]):
    cv2.rectangle( img_rgb, pt, (pt[0] + width, pt[1] + height), (0,255,255), 2)


cv2.imshow('Detected',img_rgb)
