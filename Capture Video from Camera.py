import numpy as np
import cv2 as cv

# Select capture device
choice = -1
while(not(choice <= 3 and choice >= 1)):
    choice = int(input("Enter video capture #:\n\t1 Webcam0\n\t2 Webcam1\n\t3 ./assets/testvideo.mp4\n"))
    if choice==1:
        capture = cv.VideoCapture(0)
    elif choice==2:
        capture = cv.VideoCapture(1)
    elif choice==3:
        capture = cv.VideoCapture("./assets/testvideo.mp4")


# Set resolution for display frame
frameWidth_BUFF = int(input("Input Frame Width: "))
frameHeight_BUFF = int(input("Input Frame Height: "))
ret = capture.set(cv.CAP_PROP_FRAME_WIDTH,frameWidth_BUFF)
ret = capture.set(cv.CAP_PROP_FRAME_HEIGHT,frameHeight_BUFF)
# Print resolution of display frame
print("Frame Width:", capture.get(cv.CAP_PROP_FRAME_WIDTH))
print("Frame Height:", capture.get(cv.CAP_PROP_FRAME_HEIGHT))
print("Opening capture!") 

# Check if there was an error opening capture
if not capture.isOpened():
    print("Cannot open camera")
    exit()

while capture.isOpened():
    #Capture frame-by-frame
    ret, frame = capture.read() # cap.read() returns bool and actual frame data
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(10) == ord('q'):
        break
    
#   When everything is done, release the capture
capture.release()
cv.destroyAllWindows()
