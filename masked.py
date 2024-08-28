import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("BLANK", blank)


mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)


masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("MASKED", masked)

cv.waitKey(0)
cv.destroyAllWindows()
