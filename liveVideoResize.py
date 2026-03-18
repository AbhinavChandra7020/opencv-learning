import cv2 as cv

def changeRes(width, height):
    capture.set(3, width) # 3 references width
    capture.set(4, height) # 4 references height, 10 references brightness

img =  cv.imread('photos/goku4k.png') 
capture = cv.VideoCapture('videos/cat1.mp4')
