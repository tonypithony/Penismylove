
import cv2

 
im = cv2.imread('1.jpg')
edges = cv2.Canny(im,25,255,L2gradient=False)
cv2.imwrite('ams1.png', edges)
