import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("RECTANGLE",rectangle)
cv.imshow("CIRCLE",circle)

bitand = cv.bitwise_and(rectangle,circle)
cv.imshow("BITWISE AND",bitand)

bitor=cv.bitwise_or(circle,rectangle)
cv.imshow("BITWISE OR",bitor)

bitxor=cv.bitwise_xor(circle,rectangle)
cv.imshow("BITWISE XOR",bitxor)

bitnot=cv.bitwise_not(circle)
cv.imshow("CIRCEL NOT",bitnot)

cv.waitKey(0)
cv.destroyAllWindows()