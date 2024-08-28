import cv2 as cv
import numpy as np

img=cv.imread('photos/susp.webp')
cv.imshow("NORMAL",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY",gray)

#simple thresholding
threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow("THRESHOLD",thresh)
cv.waitKey(0)