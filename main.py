import cv2
import numpy as np

# Import the function to recognize faces and path to Users json file
from recognize_faces import compareFaces
Users_json_path = "./Users.json"

# Import the function to update attendance attendance into excel
from update_attendance import update_attendance

# Load the embeddings
embeddings = np.loadtxt("./embeddings/embeddings.txt")

# Load an test image
test_image = cv2.imread('./test_images/test11.jpg')

# Check if the test_image was successfully loaded
if test_image is not None:
    print("Test Image loaded successfully.")
else:
    print("Failed to load the test image.")


''' Manual Testing Images '''
# Recognize the faces
Recognized_faces, _ = compareFaces(test_image, embeddings)
print(Recognized_faces)

update_attendance(Users_json_path, Recognized_faces)

cv2.destroyAllWindows()
