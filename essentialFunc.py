import cv2 as cv

img = cv.imread('photos/goku.png')

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat', gray)

cv.imshow('OG', img)

# blurring an image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascading
canny = cv.Canny(img, 125, 175)

# dilating the image
dilated = cv.dilate(canny, (7,7), iterations=5)

# Image erosion
eroded = cv.erode(dilated, (7,7), iterations=5)
cv.imshow('Eroded', eroded)

# resize and crop
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)