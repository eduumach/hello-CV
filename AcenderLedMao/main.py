import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

ser = serial.Serial('/dev/ttyACM0', 9600)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        l, _, _ = detector.findDistance(lmList[4], lmList[8], img)
        if l < 35:
            ser.write('b'.encode())
        else:
            ser.write('a'.encode())

    cv2.imshow("Image", img)
    cv2.waitKey(1)
