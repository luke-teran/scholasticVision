import numpy as np
import cv2 as cv


# Select capture device
capture_choice = '0'
while(not(capture_choice <= '3' and capture_choice >= '1')):
    capture_choice = input("Enter video capture #:\n\t1 Webcam0\n\t2 Webcam1\n\t3 ./assets/testvideo.mp4\n")

manipulation_choice = '0'
while(not(manipulation_choice <= '5' and manipulation_choice >= '1')):
    manipulation_choice = input("Enter image manipulation choice #:\n\t1 No manipulation\n\t2 Grayscale\n\t3 Vertical Flip\n\t4. Horizontal Flip\n\t5. Vertical & Horizontal Flip\n")

display_save_choice = '0'
while(not(display_save_choice <= '3' and display_save_choice >= '1')):
    display_save_choice = input("Enter choice #:\n\t1. Display manipulated frame\n\t2. Save modified frame\n\t3. Display & Save Modified Frame\n")
    if ((capture_choice in ['1', '2'] and display_save_choice == '2')):
        print("To save captured video, you must display it.")
        display_save_choice = '0'

# Get user inputted resolution for display frame
frameWidth_BUFF = int(input("Input Frame Width: "))
frameHeight_BUFF = int(input("Input Frame Height: "))

print("Connecting to source...")

if capture_choice == '1':
    capture = cv.VideoCapture(0)
elif capture_choice == '2':
    capture = cv.VideoCapture(1)
elif capture_choice == '3':
    capture = cv.VideoCapture("./assets/testvideo.mp4")
    
# Try to set resolution    
ret = capture.set(cv.CAP_PROP_FRAME_WIDTH,frameWidth_BUFF)
ret = capture.set(cv.CAP_PROP_FRAME_HEIGHT,frameHeight_BUFF)

# Print actual resolution of display frame
frameWIDTH_ACTUAL = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
frameHEIGHT_ACTUAL = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
print("Actual Frame Width:", frameWIDTH_ACTUAL)
print("Actual Frame Height:", frameHEIGHT_ACTUAL)

print(frameWIDTH_ACTUAL, 'x',frameHEIGHT_ACTUAL)

# Check if there was an error opening capture
if not capture.isOpened():
    print("Cannot open camera")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (frameWIDTH_ACTUAL, frameHEIGHT_ACTUAL))
print("Press the Q key to stop displaying/recording.")

SPINNER = ['|', '/', '-', '\\']
frameNumber = 0
while capture.isOpened():
    frameNumber += 1
    if(not(frameNumber%10)): print(SPINNER[int(frameNumber%8/2) ], end='\r', flush=True)    # updates spinner character every 2 frames
    
    #Capture frame-by-frame
    ret, frame = capture.read() # cap.read() returns bool and actual frame data
    
    # if frame is read correctly ret is True
    if not ret:
        print()
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Our operations on the frame come here
    if manipulation_choice == '1':
        displayframe = frame
    elif manipulation_choice == '2':
        displayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    elif manipulation_choice == '3':
        displayframe = cv.flip(frame,0)
    elif manipulation_choice == '4':
        displayframe = cv.flip(frame,1)
    elif manipulation_choice == '5':
        displayframe = cv.flip(frame,-1)

    if display_save_choice == '1':
        cv.imshow('Frame',displayframe)
        if cv.waitKey(10) == ord('q'):
            break
    elif display_save_choice in ['2','3']:
        # write the manipulated frame
        out.write(displayframe)
        
        if display_save_choice == '3':
            # Display the resulting frame
            cv.imshow('Frame',displayframe)            
            if cv.waitKey(10) == ord('q'):
                break
#   When everything is done, release the capture
#   Release everything if the job is finished
capture.release()
out.release()
cv.destroyAllWindows()