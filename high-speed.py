import cv2
import numpy as np
from matplotlib import pyplot as plt
drawing=False
ix,iy=0,0
fx,fy=0,0
img = cv2.imread("D:\\HD_A_Normal1_256\\45955.bmp")
imgdraw = np.zeros(img.shape,np.uint8)
def draw_rect(event, x, y, flags, param):
    global ix,iy,drawing,fx,fy
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        drawing = True
        newimg=img.copy()
        cv2.rectangle(newimg, (ix, iy), (x, y), (0, 255, 0), 1)
        cv2.imshow('image',newimg)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing =False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        fx,fy=x,y
        crop_img = img[iy+1:fy, ix+1:fx]
        cv2.namedWindow('imgdraw')
        cv2.imshow('imgdraw',crop_img)
        cv2.imwrite('copy.jpg',crop_img)

print type(img), type(imgdraw), img.shape, imgdraw.shape
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)

while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()



