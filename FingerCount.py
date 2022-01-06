import cv2
import time
import HandTrackingModule as htm
import pyautogui as p

#####################
wCam, hCam = 640,480
#####################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        fingers = []
        #thumb finger
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                #print("thumb finger open")
                fingers.append("acik")
        else:
            fingers.append("kapali")

        #outher fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                #print("finger open")
                fingers.append("acik")
            else:
                fingers.append("kapali")
        # print(fingers)
        
        if fingers[0] == "kapali" and fingers[1] =="kapali" and fingers[2] =="kapali" and fingers[3] =="kapali" and fingers[4] =="kapali":
            p.press("space")
            print("Baslat-Durdur")
            cv2.putText(img, "Play/Pause", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
      
        elif fingers[0] == "kapali" and fingers[1] =="acik" and fingers[2] =="kapali" and fingers[3] =="kapali" and fingers[4] =="kapali":
            p.press("down")
            print("Ses-Azaliyor")
            cv2.putText(img, "Ses Azaltiliyor", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
    
        elif fingers[0] == "kapali" and fingers[1] =="acik" and fingers[2] =="acik" and fingers[3] =="kapali" and fingers[4] =="kapali":
            p.press("up")
            print("Ses-Yukseliyor")
            cv2.putText(img, "Ses Yukseltiliyor", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
        
        elif fingers[0] == "kapali" and fingers[1] =="acik" and fingers[2] =="acik" and fingers[3] =="acik" and fingers[4] =="acik":
            p.press("right")
            print("Video-Ileri-sariliyor")
            cv2.putText(img, "Ileri Sariliyor", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
        
        elif fingers[0] == "kapali" and fingers[1] =="acik" and fingers[2] =="acik" and fingers[3] =="acik" and fingers[4] =="kapali":
            p.press("left")
            print("Video-Geri-Sariliyor")
            cv2.putText(img, "Geri Sariliyor", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
        else:
            pass
    #h, w, c = overlayList[0].shape
    #img[0:h,0:w] = overlayList[0]

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime 

    cv2.putText(img, f' FPS: {(int(fps))}', (400,50), cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)

    cv2.imshow("image", img)
    cv2.waitKey(100)
    