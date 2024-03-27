import cv2

def main():
    # Access the default camera (usually webcam)
    url = 'http://192.168.131.145/cam-hi.jpg'
    # cv2.namedWindow("Detection",cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(url)
    # cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Loop to continuously capture frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Check for keypresses and break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if _name_ == "_main_":
    main()