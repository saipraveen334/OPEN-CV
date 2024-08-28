import cv2 as cv
import numpy as np

im=cv.imread('photos/fruits.jpg')
img=cv.resize(im,(750,550),interpolation=cv.INTER_CUBIC)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("FRUITS",img)

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("BLUE",blue)
cv.imshow("GREEN",green)
cv.imshow("RED",red)
""" cv.imshow("BLUE",b)
cv.imshow("GREEN",g)
cv.imshow("RED",r) """


cv.waitKey(0)
