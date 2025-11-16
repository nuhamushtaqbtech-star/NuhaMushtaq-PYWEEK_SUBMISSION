#image reading
import cv2
image = cv2.imread(r"C:\\Users\\DELL\\OneDrive\\Desktop\\pyweek.py\\image.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
resized = cv2.resize(gray,(700,700))
blur = cv2.GaussianBlur(resized,(7,7),3)
cv2.imshow('VIRAT KOHLI',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



#video reading
#cap=cv2.VideoCapture(1)
#while True: 
   # success,frame=cap.read()
    #if not success:
        #break 
   # cv2.imshow('MY Video',frame)
   # if cv2.waitKey(0) & 0xFF==ord("q"): 
        #break
#cap.release() 
#cv2.destroyAllWindows()