import cv2


def capture_images(compareFaces, embeddings):
    print('press h for key help')

    # Open the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame")
            break
        
        cv2.imshow("Test Image",frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        elif key == ord('t'):
            cv2.waitKey(0)
            if key == ord('c'):
                continue

            elif key == ord('r'):
                Recognized_faces, Recognized_Image = compareFaces(frame, embeddings)
                cv2.imshow(Recognized_Image)
                cap.release()
                return Recognized_faces

    # # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    return None
