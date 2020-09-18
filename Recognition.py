import cv2
import numpy as np
import os 
import sqlite3

def recognise():
    conn = sqlite3.connect('attendance.db')
    cur = conn.cursor()

    # Haarcascade Classifier used for face-detection.
    face_detector= cv2.CascadeClassifier("HaarCascades/haarcascade_frontalface_default.xml");

    # LBPH Face Recognizer used for face-recognition.
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Trained/trainer.yml')

    attendance = load_workbook(filename = " ")
    sheet = attendance.active

    id = 0

    # Enter names of students in order of their ids as entered in Detection.py here.
    # names = ['None', 'Swarina', 'Paula', 'Ilza', 'Z', 'W']

    # Start realtime video capture;
    cam = cv2.VideoCapture(0)

    # Video width and Height.
    cam.set(3, 640)
    cam.set(4, 480)

    # Face-window size.
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img = cam.read()

        # Converts images to gray scale.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detects face in real-time video.
        faces = face_detector.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 6,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            # Draws rectangular box around detected face.
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Checks if confidence is less than 100.
            if confidenc >= 100:
                id = -1

            # Puts 'Present' label and name of the recognized face on the image.
            cv2.putText(img, str(id), (x+5,y+h-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 128, 255), 2)
            cv2.putText(img, str(":" + idd), (x+25,y+h-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 128, 255), 2)
            cv2.putText(img, str("Present"), (x+5,y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,204, 102), 2)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(0) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    if id == -1:
        print("Face not detected correctly. Please try again..!")
    else:
        print("\n Updating Database and Terminating program...")
        #Update 
        cur.execute("SELECT * FROM students")
        n = len(cur.fetchall())
        cur.execute("SELECT EXISTS(SELECT 1 FROM attendance WHERE date = {t})".format(t=date_today))
        if not cur.fetchone()[0]:
            cur.execute("INSERT INTO attendance VALUES({d}{x})".format(d = date_today, x=" , 0"*n))
            conn.commit()
        cur.execute("UPDATE SET '{s_roll_no}'=1 WHERE date={d}".format(s_roll_no=id,d=date_today))
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print("This module can't be run directly! :(\n")
