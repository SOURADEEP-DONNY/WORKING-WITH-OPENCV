import cv2

img=cv2.imread('lady.tiff',1) # loaded in the colour format.
cv2.imshow('l',img)
cv2.waitKey(0) # wait forever.
cv2.destroyAllWindows()

# WRITING AN IMAGE
cv2.imwrite('lady_copy.tiff',img)
