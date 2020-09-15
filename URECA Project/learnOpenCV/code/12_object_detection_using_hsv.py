import cv2 as cv
import numpy as np

def nothing(x): #simple print
    print(x)

#cv.namedWindow("Tracking")  #blank window named Tracking

while(1):
    frame = cv.imread('smarties.png')   #read image

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #example without slider - you already know the range of color for blue smarties
    l_b = np.array([110, 50, 50]) #create an array, the color of the lower bound of blue smarties HSV
    u_b = np.array([130, 255, 255])  # create an array, the color of the upper bound of blue smarties

    mask = cv.inRange(hsv, l_b, u_b)    #is the hsv color from the original image in the range set? true/false

    res = cv.bitwise_and(frame, frame, mask=mask)   #mask allows on/off of bitwise operation

    cv.imshow("frame", frame)   #show image as window "frame"
    cv.imshow("mask", mask)  # show mask, which selects bits in the range/boundary provided
    cv.imshow("res", res)  # show final result after mask

    key = cv.waitKey(1) #show for 1s per loop
    if key == 27:   #if esc, break
        break;

cv.destroyAllWindows()