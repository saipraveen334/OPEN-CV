import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

im = cv.imread('photos/cat.jpg')

img = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("BLANK", blank)

circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow("MASKED", masked)

gray_hist = cv.calcHist([img], [0], masked, [256], [0, 256])
plt.figure()
plt.title("HISTOGRAM")
plt.xlabel("BINS")
plt.ylabel("NO OF PIXELS")
plt.plot(gray_hist)
plt.xlim([0, 256])

plt.figure()
plt.title("COLOR HISTOGRAM")
plt.xlabel("BINS")
plt.ylabel("NO OF PIXELS")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([im], [i], masked, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
