import cv2 as cv
import numpy as np

""" img=cv.imread('photos/fruits.jpg')
cv.imshow("FRUITS",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY IMAGE OF FRUITS",gray) """
img2=cv.imread('photos/dog.jpg')

blur=cv.GaussianBlur(img2,(3,3),cv.BORDER_DEFAULT)
cv.imshow("BLUR",blur)

canny=cv.Canny(img2,125,175)
cv.imshow("Canny Edges",canny)

dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow("DILATED IMAGE",dilated)

eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow("ERORDED",eroded)

res=cv.resize(img2,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("RESEIZED",res)

crop=img2[50:200,200:400]
cv.imshow("CROPPED IMAGE",crop)

cv.waitKey(0)