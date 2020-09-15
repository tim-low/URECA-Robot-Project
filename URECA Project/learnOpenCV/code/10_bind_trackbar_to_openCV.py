import numpy as np
import cv2 as cv


def nothing(x):
    print(x)


#create a black image
img = np.zeros((300, 512, 3), np.uint8)
#create a blank window named 'image'
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing) #trackbar_name, window_to_add_to, startvalue, finalvalue, function_using_value
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image',img) #display image in the window
    k = cv.waitKey(1) & 0xFF    #constantly update
    if k == 27:
        break   #break if escape is pressed

    b = cv.getTrackbarPos('B', 'image') #get value of trackbar 'B' in image 'image'
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()