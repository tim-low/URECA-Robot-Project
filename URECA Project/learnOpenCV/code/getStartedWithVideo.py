import cv2

#cap = cv2.VideoCapture('video_name.avi/mp4); #for video file
cap = cv2.VideoCapture(0); #for camera index 0, -1, ect. Here 0 uses your webcam

fourcc = cv2.VideoWriter_fourcc(*'XVID') #specify the codec (for decompressing)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) #vid_name, codec, fps, video_dimensions (cap.get...WIDTH, ect)

#while True:
while (cap.isOpened()): #while capture is on, get frames
    ret, frame = cap.read() #ret is true if frame is available, and frame saves the frame itself

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #get the dimensions of video. opencv has a list of other functions
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Note: the parameters here "cap_prop_frame_width, ect" can be set as well. See 4_setting_camera_parameters_OperCV

    out.write(frame) #write the frame to the videowriter object

    #cv2.imshow('frame', frame);
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #change colour to grayscale
    cv2.imshow('frame', gray)   #show the frames in a window

    if cv2.waitKey(1) & 0xFF == ord('q'):   #if q is pressed, break loop
        break;


cap.release()   #release video resources
out.release()   #release videowriter resources
cv2.destroyAllWindows();
