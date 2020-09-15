import cv2

img = cv2.imread('lena.jpg', 1)

print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF #mask? recommended by documentation for 64bit machines

if k == 27: #press escape key
    cv2.destroyAllWindows()

elif k == ord('s'): #if value of s key is pressed)
    cv2.imwrite('lena_copy.png',img) #save image
    cv2.destroyAllWindows()