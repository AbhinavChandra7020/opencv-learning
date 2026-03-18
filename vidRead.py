import cv2 as cv

capture = cv.VideoCapture('videos/cat1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Cat', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)