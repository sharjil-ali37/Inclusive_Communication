import os
import cv2
#Setting Up Directories:
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
#Setting Parameters:
number_of_classes = 5
dataset_size = 65
#Creating Class Directories:Creates a directory for the current class inside the 'data' directory.
cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))
#User Prompt and Waiting for Key Press:
    done = False
    while not done:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "c" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)

        key = cv2.waitKey(25)
        if key == ord('c'):
            done = True
    
   #Capturing Images:
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1
#Releasing Resources:
cap.release()
cv2.destroyAllWindows()
