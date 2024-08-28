import cv2 as cv

""" img = cv.imread('photos/cat.jpg')

cv.imshow('Cat',img) """
#Reading vedios
def rescaling(frame,scale=0.50):
        width=int(frame.shape[1]*scale)
        height=int(frame.shape[0]*scale)
        dimensions=(width,height)
        return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('videos/baby.mp4')

while True:
    isTrue,frame=capture.read()
    newframe=rescaling(frame)
    cv.imshow('Baby',newframe)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()