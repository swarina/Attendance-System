# This script uses the generated dataset to train our model for face-recognition of participating users using LBPH Face Recognizer.

import cv2
import numpy as np
from PIL import Image
import os

path = 'Dataset'

# Haarcascade Classifier used for face-detection.
face_detector = cv2.CascadeClassifier("HaarCascades/haarcascade_frontalface_default.xml");

# LBPH Face Recognizer used for face-recognition.
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Function to get the images and label the data.
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        # Converts images to gray scale.
        img = Image.open(imagePath).convert('L')
        img_numpy = np.array(img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = face_detector.detectMultiScale(
            img_numpy,
            scaleFactor = 1.2,
            minNeighbors = 6,
            )

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("\n Training your data. Please wait...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Saves the model into Trained/trainer.yml
recognizer.write('Trained/trainer.yml') #

print("\n Terminating program...")
