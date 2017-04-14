import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.imread('cat.jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cat.png',img)
