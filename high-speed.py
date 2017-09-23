import cv2
import numpy as np
drawing=False
ix,iy=0,0
img = cv2.imread("D:\\HD_A_Normal1_256\\45955.bmp")
imgdraw = np.zeros(img.shape)
def draw_circle(event, x, y, flags, param):
    global ix,iy,drawing
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.line(img, (ix, iy), (x, y), (0, 255, 0), 8)
        cv2.line(imgdraw, (ix, iy), (x, y), (255, 255, 255), 4)
        ix=x
        iy=y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing =False


print type(img), type(imgdraw), img.shape, imgdraw.shape
cv2.namedWindow('image')
cv2.namedWindow('imgdraw')
cv2.setMouseCallback('image', draw_circle)
cv2.setMouseCallback('imgdraw', draw_circle)

while (1):
    cv2.imshow('image', img)
    cv2.imshow('imgdraw', imgdraw)
    if cv2.waitKey(20) & 0xFF == 27:
        cv2.imwrite('test.png', imgdraw)
        break
cv2.destroyAllWindows()



