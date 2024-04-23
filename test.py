import cv2


def capture_images():
    print('press h for key help')

    # Open the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    while True:
        # Wait for user input
        key = cv2.waitKey(100)

        # Press 't' to capture image
        if key == ord('t'):
            # Capture frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to capture frame.")
                break

            # Display the captured image
            cv2.imshow('Captured Image', frame)

        # Press 'c' to continue capturing next image
        elif key == ord('c'):
            continue

        # Press 'q' to quit
        elif key == ord('q'):
            break

        # Press any other key to display the help message
        elif key == ord('h'):
            print("Press 't' to capture image.")
            print("Press 'c' to capture next image.")
            print("Press 'q' to quit.")

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


# Call the function to capture images
capture_images()
