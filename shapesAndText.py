import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)

cv.rectangle(blank, (250,0), (500,250), (255,0,0), thickness=-1)

cv.rectangle(blank, (0,500), (250,250), (0,255,255), thickness=-1)

cv.rectangle(blank, (250,250), (500,500), (255,0,255), thickness=-1)

# draw a circle
cv.circle(blank, ((blank.shape[1]//2, blank.shape[0]//2)), 200, (0, 0, 255), thickness = -1)

# draw a line
cv.line(blank, (0,250), (500,250), (255,255,255), thickness=3)
cv.line(blank, (250,0), (250,500), (255, 255, 255), thickness=3)

# write text on an image
cv.putText(blank, ' Hello', (200,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 0), 2)

cv.imshow('Line', blank)

cv.waitKey(0)