import cv2

img=cv2.imread('lady.tiff',1) # loaded in the colour format.
cv2.imshow('l',img)
k=cv2.waitKey(0) # wait forever.
if k==27: # TO DELETE ENTER ESCAPE BUTTON
    cv2.destroyAllWindows()
elif k==ord('s'):# TO SAVE A COPY BY WRITING AN IMAGE PRESS 'S' KEY.
    cv2.imwrite('lady_copy.tiff', img)
cv2.destroyAllWindows()#OTHERWISE ALL COPIES DESTROYED.