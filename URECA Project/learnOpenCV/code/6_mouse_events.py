import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]  #dir shows all classes and member functions in package.
                                                #we want to find events. mouse buttons are events
#print(events)



def click_event(event, x, y, flags, param): #event (eg. leftclick), coord_x, coord_y, not sure what flag/param are)
    if event == cv2.EVENT_LBUTTONDOWN: #write coordinates on image
        print(x, ',  ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.5, (255,255,0), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN: #write colour of pixel on image
        blue = img[y, x, 0] #B, G, R in that order
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event) #window_name, callback_function

cv2.waitKey(0)
cv2.destroyAllWindows()