import numpy as np
import cv2 # Import the OpenCV library


def preprocess_image(img):
    # Convert the image to grayscale using OpenCV
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    # Resize the grayscale image using OpenCV
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    # Apply adaptive thresholding to the resized image using OpenCV
    processed_image = cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )
    return processed_image



