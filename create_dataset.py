# Import necessary libraries
import cv2
import os

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create a directory for storing the dataset
if not os.path.exists("dataset"):
    os.makedirs("dataset")

# Create a dataset
count = 0
while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.waitKey(1) == ord('s'):
        count += 1
        filename = "dataset/user_" + str(count) + ".jpg"
        cv2.imwrite(filename, frame)

cap.release()
cv2.destroyAllWindows()