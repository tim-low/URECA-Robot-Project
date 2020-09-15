import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]  #dir shows all classes and member functions in package.
                                                #we want to find events. mouse buttons are events
#print(events)


'''
def click_event(event, x, y, flags, param): #event (eg. leftclick), coord_x, coord_y, not sure what flag/param are)
    if event == cv2.EVENT_LBUTTONDOWN: #draw and connect points
        cv2.circle(img, (x, y), 3, (0,0,255), -1)   #draw a circle when you click
        points.append((x,y))    #keep a list of points
        if len(points) >= 2:    #if there is more than one point on the page
            cv2.line(img, points[-1], points[-2], (255,0,0), 5) #draw a line between the last two points
        cv2.imshow('image', img) '''

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: #display coordinates in another windows
        blue = img[y, x, 0] #colour channels
        green = img[y, x, 1]
        red = img[y, x, 2]
        #cv2.circle(img, (x, y), 3, (0,0,255), -1) #
        myColorImage = np.zeros((512,512, 3), np.uint8) #new image to display color
        myColorImage[:] = [blue, green, red] #fill all pixels with this color

        cv2.imshow('color', myColorImage)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

points = []

cv2.setMouseCallback('image', click_event) #window_name, callback_function

cv2.waitKey(0)
cv2.destroyAllWindows()