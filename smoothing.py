import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')

average = cv.blur(img, (3, 3))
median = cv.medianBlur(img, 3)
gauss = cv.GaussianBlur(img, (3, 3), 1)
bi = cv.bilateralFilter(img, d=10, sigmaColor=30, sigmaSpace=20)

cv.imshow("AVERAGE BLUR", average)
cv.imshow("MEDIAN BLUR", median)
cv.imshow("GAUSSIAN BLUR", gauss)
cv.imshow("BILATERAL BLUR", bi)

cv.waitKey(0)
cv.destroyAllWindows()
