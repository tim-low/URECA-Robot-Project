import numpy as np
import cv2 as cv


def nothing(x):
    print(x)



#create a blank window named 'image'
cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing) #trackbar_name, window_to_add_to, startvalue, finalvalue, function_using_value

switch = 'color/grayscale'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('lena.jpg') #read image constantly in while loop. previously not needed because we overwrote every pixel

    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50,150), font, 6, (0,0,255), 10)

    k = cv.waitKey(1) & 0xFF    #constantly update
    if k == 27:
        break   #break if escape is pressed


    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.imshow('image',img) #display image in the window
cv.destroyAllWindows()