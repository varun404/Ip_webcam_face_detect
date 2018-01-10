import cv2
import numpy as np
import urllib

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#Enter your Ip webcam address here.
url = "http://192.168.1.104:8080/shot.jpg"


while True:
	#Open url
    imgresp = urllib.urlopen(url)
	#Convert image into numpy byte array as cvtColor requires  array as input
    imgnp = np.array(bytearray(imgresp.read()), dtype=np.uint8)
	#Decode it so that it is readable as cv2 image(Which is a numpy array now)
    img = cv2.imdecode(imgnp, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale((roi_gray))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if  k == 27:
        break

cap.release()
cv2.destroyAllWindows()





