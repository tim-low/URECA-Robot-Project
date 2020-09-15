import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', -1)
cv.imshow('image', img)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)    #matplotlib uses RGB, cv2 uses BGR
plt.imshow(img)
plt.show()  #matplotlib has cool things like coordinates and positioning

cv.waitKey(0)
cv.destroyAllWindows()