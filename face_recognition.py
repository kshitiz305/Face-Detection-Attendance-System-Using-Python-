
import cv2

# Import numpy for matrices calculations
import numpy as np
import xlwrite
import time
import sys
import os 

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

start = time.time()
period = 8
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("trainer/")

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
flag = 0;
id = 0;
filename = 'filename';
dict = {
    'item1': 1
}

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check the ID if exist 
        if (confidence < 50):
            if(Id == 1):
                Id = "Kshitiz {0:.2f}%".format(round(100 - confidence, 2))
                if ((str(Id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 2, Id, 'yes');
                    dict[str(Id)] = str(Id);

            elif(Id == 2):
                Id = "Shiv {0:.2f}%".format(round(100 - confidence, 2 ))
                if ((str(Id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 1, Id, 'yes');
                    dict[str(Id)] = str(Id);

            elif (Id == 3):
                Id = "Richa {0:.2f}%".format(round(100 - confidence, 2))
                if ((str(Id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 3, Id, 'yes');
                    dict[str(Id)] = str(Id);

            elif (Id == 4):
                Id = "Sameer {0:.2f}%".format(round(100 - confidence, 2))
                if ((str(Id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 4, Id, 'yes');
                    dict[str(Id)] = str(Id);

            elif (Id == 7):
                Id = "Simran {0:.2f}%".format(round(100 - confidence, 2))
                if ((str(Id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 4, Id, 'yes');
                    dict[str(Id)] = str(Id);

        else:
            Id="unknown"
        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im)

    # if flag == 10:
    #     print("Transaction Blocked")
    #     break;
    # if time.time() > start + period:
    #     break;

    # If 'q' is pressed, close program
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
