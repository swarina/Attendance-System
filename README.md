# Attendance-System

An attendance system program which recognizes users' faces and automatically marks them present for their corresponding names and roll number in the existing attendance database.

## About

This system uses the **HaarCascade classifier** for face-detection and **LBPH face-recognition** algorithm for face-recognition.  
  
A database is initialised in the beginning of the program as *database.db*. Students are added with their names,roll numbers and sample pictures are captured from real-time video which are saved in the *Dataset* folder. Later a *trainer.yml* file is created in the *Trained* folder based on the existing dataset. The LBPH face-recognizer uses the same to detect and recognize faces from real-time video and accordingly marks them present in the Attendance table.

### Libraries

 This script is entirely written in python using the following libraries:
 - OpenCV
 - Numpy
 - Pillow
 - Sqlite3
 
 
 
 
