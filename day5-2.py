import cv2
import ultralytics
from ultralytics import YOLO
model =YOLO('yolo11n.pt') 
cap=cv2.VideoCapture(1) 
while True:
    success,frame=cap.read()
    cv2.flip(frame,1,frame)
    if not success:
        break
    results=model(frame)
    annotated_frame=results[0].plot()
    cv2.imshow("OBJECT DETECTION",annotated_frame)
    if cv2.waitkey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()