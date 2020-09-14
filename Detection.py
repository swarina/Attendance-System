import cv2

# Start real-time video.
cam = cv2.VideoCapture(0)

# Video width and Height.
cam.set(3, 640)
cam.set(4, 480)

# Haarcascade Classifier used for face detection.
face_detector = cv2.CascadeClassifier('HaarCascades/haarcascade_frontalface_default.xml')

#Roll No. for each student.
face_id = input('\n Enter Roll No.: ')

print("\n Initializing face capture. Look at the camera and wait ...")

# Counter for each sample picture captured.
count = 0

# Face-window size:
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while(True):

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

    for (x,y,w,h) in faces:

        # Draws rectangular box around detected face.
        cv2.rectangle(img, (x,y), (x+w,y+h), (0, 204, 102), 2)     
        count += 1

        # Captured image saved in Dataset folder.
        cv2.imwrite("Dataset/Student." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

    k = cv2.waitKey(0) & 0xff # Press 'ESC' to exit video.
    if k == 27:
        break
    elif count >= 30: # Captures 30 face sample and exits video.
         break

print("\n Terminating program...")
cam.release()
cv2.destroyAllWindows()