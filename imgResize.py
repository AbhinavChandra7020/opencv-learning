import cv2 as cv

def resizeImage(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img =  cv.imread('photos/goku4k.png') 

cv.imshow('GOKU', img)   
cv.imshow('GOKU_RESIZED', resizeImage(img, 5))            

cv.waitKey(0)