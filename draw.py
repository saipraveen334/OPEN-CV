import cv2 as cv
import numpy as np


#Creating a blank image
blank=np.zeros((500,500,3),dtype='uint8')
"""cv.imshow('BLANK',blank)
blank[:]=0,255,0
cv.imshow("GREEN",blank) 
cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,0,255),thickness=-1)
cv.circle(blank,((blank.shape[0]//2),(blank.shape[1]//2)),40,(255,0,0),thickness=-1 )
cv.line(blank,(0,0),((blank.shape[0]//2),(blank.shape[1]//2)),(255,255,255),thickness=3)
cv.imshow("PAINT",blank) """
cv.putText(blank,"Sai Praveen",((blank.shape[0]//2),(blank.shape[1]//2)),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),2)
cv.imshow("TEXT",blank)
cv.waitKey(0)
