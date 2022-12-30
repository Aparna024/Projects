import cv2
import os
import shutil
filename = r"C:\Users\Aparna\Downloads\abc.mp4"
if os.path.exists('output'):
    shutil.rmtree('output') # We are creating a directory to define the path to store the output frames

os.makedirs('output')

captured = cv2.VideoCapture(filename)
# cap = cv2.VideoCapture(0)
count = 0
while captured.isOpened():
    ret,frame = captured.read()
    if ret == True:
        cv2.imshow('window-name',frame)
        cv2.imwrite("C:.output/frame%d.jpg" % count, frame)
        count = count + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
captured.release()
cv2.destroyAllWindows()