import cv2
import datetime


cap = cv2.VideoCapture(0)
print(cap.get(3))   #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Numbers represent the parameter
print(cap.get(4))   #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 3000)        #despite setting it, the camera sets to an available resolution (eg. 1204 --> 1280:720)
cap.set(4, 3000)
print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()): #while capture is on, get frames
    ret, frame = cap.read() #ret is true if frame is available, and frame saves the frame itself
    if ret:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA) #write text. image, text, location, font, font_size, color, thickness, antialiasing
        frame = cv2.putText(frame, datet, (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)  # write text. image, text, location, font, font_size, color, thickness, antialiasing

        cv2.imshow('frame', frame)   #show the frames in a window
        if cv2.waitKey(1) & 0xFF == ord('q'):   #if q is pressed, break loop
            break;
    else:
        break;

cap.release()   #release video resources

cv2.destroyAllWindows();
