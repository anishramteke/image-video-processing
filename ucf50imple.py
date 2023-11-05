import cv2
import os

# Specify the path to the directory containing UCF50 dataset
dataset_path = "minor project/UCF50"

# List all subdirectories (each representing an action category)
action_categories = os.listdir(dataset_path)

#Thinning Algorithm
def thinning(image):
    image = image.astype(np.uint64) 
    while True:
        # Step 1
        marker = np.zeros_like(image)
        for x in range(1, image.shape[0] - 1):
            for y in range(1, image.shape[1] - 1):
                p2 = image[x - 1, y]
                p3 = image[x - 1, y + 1]
                p4 = image[x, y + 1]
                p5 = image[x + 1, y + 1]
                p6 = image[x + 1, y]
                p7 = image[x + 1, y - 1]
                p8 = image[x, y - 1]
                p9 = image[x - 1, y - 1]
                A = (p2 == 0 and p3 == 1) + (p3 == 0 and p4 == 1) + (p4 == 0 and p5 == 1) + (p5 == 0 and p6 == 1) + (p6 == 0 and p7 == 1) + (p7 == 0 and p8 == 1) + (p8 == 0 and p9 == 1) + (p9 == 0 and p2 == 1)
                B = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
                m1 = (p2 * p4 * p6)
                m2 = (p4 * p6 * p8)
                if 2 <= B <= 6 and A == 1 and (m1 == 0 or m2 == 0):
                    marker[x, y] = 1

        image &= ~marker

        # Step 2
        marker = np.zeros_like(image)
        for x in range(1, image.shape[0] - 1):
            for y in range(1, image.shape[1] - 1):
                p2 = image[x - 1, y]
                p3 = image[x - 1, y + 1]
                p4 = image[x, y + 1]
                p5 = image[x + 1, y + 1]
                p6 = image[x + 1, y]
                p7 = image[x + 1, y - 1]
                p8 = image[x, y - 1]
                p9 = image[x - 1, y - 1]
                A = (p2 == 0 and p3 == 1) + (p3 == 0 and p4 == 1) + (p4 == 0 and p5 == 1) + (p5 == 0 and p6 == 1) + (p6 == 0 and p7 == 1) + (p7 == 0 and p8 == 1) + (p8 == 0 and p9 == 1) + (p9 == 0 and p2 == 1)
                B = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
                m1 = (p2 * p4 * p8)
                m2 = (p2 * p6 * p8)
                if 2 <= B <= 6 and A == 1 and (m1 == 0 or m2 == 0):
                    marker[x, y] = 1


# Loop through each action category
for category in action_categories:
    category_path = os.path.join(dataset_path, category)
    
    # List all video files in the current category
    video_files = [f for f in os.listdir(category_path) if f.endswith(".avi") or f.endswith(".mp4")]
    
    # Loop through each video file in the current category
    for video_file in video_files:
        video_path = os.path.join(category_path, video_file)
        video_capture = cv2.VideoCapture(video_path)

        while True:
            # Read a frame from the video
            ret, frame = video_capture.read()

            # Break the loop if we have reached the end of the video
            if not ret:
                break

            # Convert the frame to grayscale and apply processing (same as your original code)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, binary_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
            thinned_frame = cv2.ximgproc.thinning(binary_frame)

            # Display frames (optional)
            cv2.imshow("Original Frame", frame)
            cv2.imshow("Thinned Frame", thinned_frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release video capture for the current video file
        video_capture.release()

    # Release video capture for the current category
    cv2.destroyAllWindows()
