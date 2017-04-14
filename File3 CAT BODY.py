import cv2
import numpy as np

img = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)

cat_body = img[150:500,220:620]
cv2.imshow('image',cat_body)
cv2.waitKey(0)

img[0:350,0:400] = cat_body
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
