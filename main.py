import cv2 as cv #25bce2411 tanvi
import numpy as np
import mediapipe as mp

capture=cv.VideoCapture(0)

shape=(480,640,3)
mask=np.zeros(shape,np.uint8)
colour=(255,0,255)
thickness=5
mp_hands= mp.solutions.hands
draw=mp.solutions.drawing_utils
landmarks=mp_hands.Hands(max_num_hands=1)
prevxy=None
while True:
    
    isTrue,frame=capture.read()
    
    rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    op=landmarks.process(rgb)
    
    if op.multi_hand_landmarks:
        for i in op.multi_hand_landmarks:
            draw.draw_landmarks(frame,i,mp_hands.HAND_CONNECTIONS)
            x=int(i.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*shape[1])
            y=int(i.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*shape[0])
            if prevxy!=None:
                cv.line(mask,prevxy,(x,y),colour,thickness)
            prevxy=(x,y)
    frame=np.where(mask,mask,frame)
    if isTrue:
        if cv.waitKey(1)==ord('q'):
            break
        else:
            cv.imshow('frame',frame)
capture.release()
cv.destroyAllWindows()


