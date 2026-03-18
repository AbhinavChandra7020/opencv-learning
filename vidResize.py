import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('videos/cat1.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("Video ended or file not found.")
        break

    frame_resized = rescaleFrame(frame, 0.66)

    cv.imshow('Cat', frame)
    cv.imshow('Cat Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()