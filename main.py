import cv2 as cv

img =  cv.imread('photos/cat1.png') # read the image

cv.imshow('cat', img)               # display the image

cv.waitKey(0)