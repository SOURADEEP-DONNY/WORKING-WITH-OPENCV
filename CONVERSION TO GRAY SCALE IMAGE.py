import cv2
#READING AN IMAGE AND SHOWING AN IMAGE.
img=cv2.imread('lady.tiff',0)
cv2.imshow('grayscale image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

