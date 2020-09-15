import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  #if below 127, becomes 0, otherwise 1 (binary threshold). Use for masks
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)  #inverse
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)  #unchanged until after threshold, remains constant
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  #before threshold, change to zero
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)  #after thresthold, change to zero

titles = ['Original Image', 'Binary', 'Bin_Inv', 'Trunc', 'ToZero', 'ToZero_Inv']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray') #2, by 3, position=index+1, plot_respective_image
    plt.title(titles[i])    #plot_respective_title
    plt.xticks([]), plt.yticks([])  #remove ticks --> empty list for xticks, yticks

plt.show()
#cv.imshow("Image", img)
#cv.imshow("TH1", th1)
#cv.imshow("TH2", th2)
#cv.imshow("TH3", th3)
#cv.imshow("TH4", th4)
#cv.imshow("TH5", th5)


cv.waitKey(0)
cv.destroyAllWindows()