import cv2 as cv 
import numpy as np

img=cv.imread('photos/a.jpeg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY",gray)

#LAPLACIAN
lap=cv.Laplacian(gray,cv.CV_64F)
np=np.uint8(np.absolute(lap))
cv.imshow("LAP",lap)

cv.waitKey(0)
