import cv2 as cv #25bce2411 tanvi
import numpy as np
import mediapipe as mp

capture=cv.VideoCapture(0)
while True:
    
    isTrue,frame=capture.read()
    rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    mp_hands= mp.solutions.hands
    draw=mp.solutions.drawing_utils
    landmarks=mp_hands.Hands(max_num_hands=1)
    op=landmarks.process(rgb)
    if op.multi_hand_landmarks:
        for i in op.multi_hand_landmarks:
            draw.draw_landmarks(frame,i,mp_hands.HAND_CONNECTIONS)

    if isTrue:
        if cv.waitKey(1)==ord('q'):
            break
        else:
            cv.imshow('frame',frame)
capture.release()
cv.destroyAllWindows()

