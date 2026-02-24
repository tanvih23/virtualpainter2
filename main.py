import cv2 as cv #25bce2411 tanvi
import numpy as np
import mediapipe as mp

capture=cv.VideoCapture(0)
wdth=int(capture.get(3))
ht=int(capture.get(4))
shape=(wdth,ht,3)
mask=np.zeros(shape,np.uint8)
colour=(255,0,0)
thickness=5
while True:
    
    isTrue,frame=capture.read()
    
    rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    mp_hands= mp.solutions.hands
    draw=mp.solutions.drawing_utils
    landmarks=mp_hands.Hands(max_num_hands=1)
    op=landmarks.process(rgb)
    prevxy=None
    if op.multi_hand_landmarks:
        for i in op.multi_hand_landmarks:
            draw.draw_landmarks(frame,i,mp_hands.HAND_CONNECTIONS)
            x=int(i.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*wdth)
            y=int(i.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*ht)
            if prevxy!=None:
                cv.line(mask,prevxy,(x,y),colour,thickness)
            
    if isTrue:
        if cv.waitKey(1)==ord('q'):
            break
        else:
            cv.imshow('frame',frame)
capture.release()
cv.destroyAllWindows()


