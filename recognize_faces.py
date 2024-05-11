import face_recognition
import cv2
import json


def compareFaces(Image, embeddings):
    recognized_users = []

    # Load the Registered users json file
    jsonFilePath = "./Users.json"
    with open(jsonFilePath, "r") as Users:
        Users = json.load(Users)

    face_locations = face_recognition.face_locations(Image)
    face_encodings = face_recognition.face_encodings(Image, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(embeddings, face_encoding)

        # If the face encoding matches any index in embeddings
        if True in matches:
            index = matches.index(True)
            name = "user_" + str(index+1)
            recognized_users.append(Users[name])

            # Drawing a rectangle and the name around the recognized face
            cv2.rectangle(Image, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(Image, Users[name], (left, top-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    Image = cv2.resize(Image, (1600, 720))
    # cv2.imshow("Recognized_Image", Image)
    # cv2.waitKey(0)

    # Return the list of recognized users and the Image with rectangles draw
    return recognized_users, Image
