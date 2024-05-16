import numpy as np
import cv2 as cv



def nothing(x):
    pass


# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy, drawing, mode
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix,iy), (x,y), (b,g,r),border_size)
            else:
                cv.circle(img, (x,y), brush_size, (b,g,r),border_size)
                
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(b,g,r),0)
        else:
            cv.circle(img,(x,y),brush_size,(b,g,r),border_size)
            

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# Create a black image, a window
img = 255 * np.ones((300,512,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('Brush Sz','image',0,50,nothing)
cv.createTrackbar('Border Sz','image',0,100,nothing)

# create switch for ON/OFF functionality
switch = 'Clear Bttn'
cv.createTrackbar(switch, 'image',1,1,nothing)

while(1):
    cv.imshow('image',img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
    
    # get current position of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    brush_size = cv.getTrackbarPos('Brush Sz','image')
    border_size = cv.getTrackbarPos('Border Sz','image')

    
    if s == 0:
        print("Cleared painting!")
        cv.setTrackbarPos(switch, 'image', 1)
        img[:] = (255,255,255)
    else:
        cv.setMouseCallback('image',draw_circle)
        cv.imshow('image',img)
        key = cv.waitKey(1) & 0xFF
        if key == ord('m'):
            mode = not(mode)
        elif key == 27:
            break
        # img[:] = [b,g,r]

cv.destroyAllWindows()