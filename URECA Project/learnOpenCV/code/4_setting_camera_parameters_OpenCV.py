import cv2

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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #change colour to grayscale
        cv2.imshow('frame', gray)   #show the frames in a window

        if cv2.waitKey(1) & 0xFF == ord('q'):   #if q is pressed, break loop
            break;
    else:
        break;

cap.release()   #release video resources

cv2.destroyAllWindows();
