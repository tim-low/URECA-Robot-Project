import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)  #image in color
img = np.zeros([512, 512, 3], np.uint8) #create blank image. dimensions, specify datatype (eg. double, uint8)

img = cv2.line(img, (0,0), (255,255), (0,0,255), 5) #draw a line. image, start_coord, end_coord, color, thickness
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 5)
img = cv2.rectangle(img, (384,0), (510, 128), (0,0,255), 10) #draw a rectangle. image, top_left, bot_right, color, thickness. fill with thick=-1
img = cv2.circle(img, (447,63), 63, (0,255,0), -1)  #draw a circle. image, centre, radius, color, thickness = fill)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Writing text on u', (10,500), font, 1, (255,255,255), 2, cv2.LINE_AA) #write text. image, text, location, font, font_size, color, thickness, antialiasing


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()