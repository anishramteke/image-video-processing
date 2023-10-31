import cv2

# Open the video file
video_capture = cv2.VideoCapture("minor project/istockphoto-1166698457-640_adpp_is.mp4")  # Update with the path to your input video file

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Break the loop if we have reached the end of the video
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding to create a binary image
    _, binary_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

    # Apply thinning algorithm
    thinned_frame = cv2.ximgproc.thinning(binary_frame)

    # Display the original and thinned frames (optional)
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Thinned Frame", thinned_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()
