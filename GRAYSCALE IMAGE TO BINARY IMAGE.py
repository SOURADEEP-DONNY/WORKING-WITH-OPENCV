import cv2
img=cv2.imread('lady.tiff',0)
cv2.imshow('grayscale_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#THRESHOLDING
ret, bw=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow('BINARY IMAGE',bw)
cv2.waitKey(0)
cv2.destroyAllWindows()