import cv2 as cv

img =  cv.imread('photos/goku4k.png') # read the image

cv.imshow('GOKU', img)               # display the image

cv.waitKey(0)