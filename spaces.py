import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


im=cv.imread('photos/fruits.jpg')
img=cv.resize(im,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("FRUITS",img)

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.imshow(grey)
plt.show()
""" gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)
cv.imshow("GRAY",gray)
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow("LAB",lab)"""
cv.waitKey(0)