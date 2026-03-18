import cv2 as cv
import numpy as np

cat = cv.imread('photos/cat1.png')
goku = cv.imread('photos/goku.png')

cv.imshow('Cat', cat)

# translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)

# -x (negative x) --> translate image to left
# -y (negative y) --> translate image to up
# x (positive x) --> translate image to right
# y (positive y) --> translate image down 

translate = translate(cat, -100, -100)
cv.imshow('Translate', translate)

# rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = width,height

    return cv.warpAffine(img,rotMat, dimensions)

rotate = rotate(cat, 90)
cv.imshow('Rotated', rotate)

# flipping
flip = cv.flip(cat, -1) # 0 -> vertical, 1 -> horizontal, -1 -> both ways
cv.imshow('flip', flip)
 
cv.waitKey(0)
