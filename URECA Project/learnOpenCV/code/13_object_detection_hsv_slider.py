import cv2 as cv
import numpy as np

def nothing(x): #simple print
    pass

cap = cv.VideoCapture(0)


cv.namedWindow("Tracking")  #blank window named Tracking
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)    #lower color value
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)    #upper value
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)    #lower hue
cv.createTrackbar("UH", "Tracking", 179, 179, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)    #lower sat
cv.createTrackbar("US", "Tracking", 255, 255, nothing)

while(1):
    frame = cv.imread('smarties.png')   #read image
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #example with slider
    l_v = cv.getTrackbarPos('LV', "Tracking")
    u_v = cv.getTrackbarPos('UV', "Tracking")
    l_h = cv.getTrackbarPos('LH', "Tracking")
    u_h = cv.getTrackbarPos('UH', "Tracking")
    l_s = cv.getTrackbarPos('LS', "Tracking")
    u_s = cv.getTrackbarPos('US', "Tracking")

    l_b = np.array([l_h, l_s, l_v]) #create an array, the color of the lower bound of blue smarties HSV
    u_b = np.array([u_h, u_s, u_v])  # create an array, the color of the upper bound of blue smarties

    mask = cv.inRange(hsv, l_b, u_b)    #is the hsv color from the original image in the range set? true/false

    res = cv.bitwise_and(frame, frame, mask=mask)   #mask allows on/off of bitwise operation

    cv.imshow("frame", frame)   #show image as window "frame"
    cv.imshow("mask", mask)  # show mask, which selects bits in the range/boundary provided
    cv.imshow("res", res)  # show final result after mask

    key = cv.waitKey(1) #show for 1s per loop
    if key == 27:   #if esc, break
        break;

cap.release()
cv.destroyAllWindows()