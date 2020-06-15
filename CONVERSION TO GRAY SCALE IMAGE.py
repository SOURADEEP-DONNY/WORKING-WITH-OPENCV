import cv2
#READING AN IMAGE AND SHOWING AN IMAGE.
img=cv2.imread('lady.tiff')
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#CONVERTING THE IMAGE TO GRAYSCALE IMAGE FROM COLOUR MAGE
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayimage',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
