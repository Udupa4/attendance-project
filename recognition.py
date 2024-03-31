# Import necessary libraries
import cv2
import face_recognition
# from face_recognition.api import face_locations, compare_faces, face_encodings
import numpy as np
import os
import json
from datetime import datetime

# Load the embeddings
embeddings = np.loadtxt("embeddings/embeddings.txt")

# Initialize the camera
cap = cv2.VideoCapture(0)

# Load the attendance log
if not os.path.exists("attendance.json"):
    with open("attendance.json", "w") as f:
        json.dump({}, f)
with open("attendance.json", "r") as f:
    attendance = json.load(f)

# Load an test image
test_image = cv2.imread(
    'C:/Users/Nishanth/Desktop/Auto-Attendance_Cognitive/Smart_Attendance_System/test_images/test11.jpg')

# Check if the test_image was successfully loaded
if test_image is not None:
    print("Test Image loaded successfully.")
else:
    print("Failed to load the test image.")

# Recognize the faces and mark attendance
# while True:
#     ret, frame = cap.read()
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(embeddings, face_encoding)
#         if True in matches:
#             index = matches.index(True)
#             name = "user_" + str(index+1)
#             if name not in attendance:
#                 attendance[name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 with open("attendance.json", "w") as f:
#                     json.dump(attendance, f)
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             cv2.putText(frame, name, (left, top-10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#     cv2.imshow("frame", frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

''' Manual Testing Images '''
# Recognize the faces
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(embeddings, face_encoding)
    if True in matches:
        index = matches.index(True)
        name = "user_" + str(index+1)
        if name not in attendance:
            attendance[name] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            # attendance[name] = "02-04-2024 13:22:53"
            with open("attendance.json", "w") as f:
                json.dump(attendance, f)
        cv2.rectangle(test_image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(test_image, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
test_image = cv2.resize(test_image, (1600, 720))
cv2.imshow("test_image", test_image)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
