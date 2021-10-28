#import cv2
import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640) #lebar  cam
cam.set(4, 480) #tinggi cam
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    retV, frame = cam.read()
    Grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(Grey, 1.3, 5) #frame, scaleFactor,
    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+y, y+h),(0,255,255), 2)
    cv2.imshow('Camera', frame)
    #cv2.imshow('webcamku 2', Grey)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()