import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)

    if len(lmList) != 0:
        print(lmList[8])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (20, 30), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 255, 255), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
