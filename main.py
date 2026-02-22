import cv2 as cv
import numpy as np
capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    if isTrue:
        if cv.waitKey(1)==ord('q'):
            break
        else:
            cv.imshow('frame',frame)
capture.release()
cv.destroyAllWindows()

