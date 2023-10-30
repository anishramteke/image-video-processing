import cv2
import numpy as np
import threading

# ... (your existing functions remain unchanged)

def openImage(path):
    img = cv2.imread(path)
    return img

def getBlackWhiteImage(img):
    lin, col = img.shape
    img2 = np.zeros((lin,col,1), dtype=np.uint8)
    for i in range(lin):
        for j in range(col):
            if img[i][j] < 200:
                img2[i][j] = 0
            else:
                img2[i][j] = 255
    return img2

def process_rows(start, end, img, result):
    for row in range(start, end):
        for col in range(1, img.shape[1] - 1, 1):
            # ... (your existing processing logic here)
            result[start:end] = img[start:end]

def parallel_thinning(img, num_threads=4):
    rows, cols, _ = img.shape
    chunk_size = rows // num_threads
    threads = []
    results = [None] * rows

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else rows
        thread = threading.Thread(target=process_rows, args=(start, end, img.copy(), results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return np.array(results)

def main():
    originalImage = openImage("C:\\Users\\Anish\\Downloads\\_98be8ee7-83c5-41a3-8512-911c3d18ae60.jpg")
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    BWimage = getBlackWhiteImage(grayImage)
    thinningImage = parallel_thinning(BWimage)
    cv2.imshow("Original Image", originalImage)
    cv2.imshow("Black and White Image", BWimage)
    cv2.imshow("Thinning Image", thinningImage)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
