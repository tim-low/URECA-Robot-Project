import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) #tuple of row, column, color_channels in the image
print(img.size) #total number of pixels
print(img.dtype) #image datatype
b,g,r = cv2.split(img) #splits into each color channel, an array for each pixel
img = cv2.merge((b,g,r))    #merges color channels into single image, 3 arrays into an image

ball = img[280:340, 330:390] #upper left of ball, lower right of ball
img[273:333, 100:160] = ball #copy ball and paste it in this coordinate range

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
#dst = cv2.add(img,img2)   #combine images by adding their values
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)   #combine images with different weight to each image

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()