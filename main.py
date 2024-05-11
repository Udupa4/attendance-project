import cv2
import numpy as np

# Import the function to recognize faces
from recognize_faces import compareFaces

# Import path to Users json file
Users_json_path = "./Users.json"

# Import the test function to capture images
from test import capture_images

# Import the function to update attendance attendance into excel
from update_attendance import update_attendance

# Load the embeddings
embeddings = np.loadtxt("./embeddings/embeddings.txt")

# # Load an test image
# test_image = cv2.imread('./test_images/test11.jpg')

# # Check if the test_image was successfully loaded
# if test_image is not None:
#     print("Test Image loaded successfully.")
# else:
#     print("Failed to load the test image.")


''' Manual Testing Images '''
# # Recognize the faces
# Recognized_faces, _ = compareFaces(test_image, embeddings)
# print(Recognized_faces)

Recognized_faces = capture_images(compareFaces, embeddings)

if Recognized_faces is not None:
    update_attendance(Users_json_path, Recognized_faces)
    print(Recognized_faces)

else: print("Error:Could not Recognize face")

cv2.destroyAllWindows()
