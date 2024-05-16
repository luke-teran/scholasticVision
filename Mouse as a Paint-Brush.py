import numpy as np
import cv2 as cv

# mouse callback function
def draw_crosshair(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        crosshair_radius = 100
        half_size = crosshair_radius // 2

        cv.circle(img,(x,y),crosshair_radius,(0,0,255),5)
        cv.line(img, (x - crosshair_radius,y), (x + crosshair_radius, y), (255,255,255),1)
        cv.line(img, (x, y - crosshair_radius), (x, y + crosshair_radius), (255,255,255),1)
        
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
#cv.setMouseCallback('image',draw_circle)
cv.setMouseCallback('image',draw_crosshair)

events = [i for i in dir(cv) if 'EVENT' in i]
print( events )

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xF == 27:
        break

cv.destroyAllWindows()