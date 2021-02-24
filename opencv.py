import cv2 
import os

try:
    os.remove("Output.avi")
except:
    pass

vid = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frameslist=list()
out = cv2.VideoWriter('Output.avi',fourcc, 30.0, (640,480))
while(True): 
	
    ret, frame = vid.read()
    if ret: 
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow('frame', frame)
        out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release()
out.release() 
cv2.destroyAllWindows() 