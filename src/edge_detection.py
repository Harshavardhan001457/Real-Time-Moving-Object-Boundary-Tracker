import cv2
import numpy as np


def detect_edges( gray_frame: np.ndarray,low_threshold = 50,high_threshold = 150,blur_kernel= (5, 5)):

    # Safety check
    if gray_frame is None or len(gray_frame.shape) != 2:
        raise ValueError("detect_edges expects a valid grayscale image")

    #Reducing the noise before edge detection
    blurred = cv2.GaussianBlur(gray_frame, blur_kernel, 0)

    #Canny edge detection
    edges = cv2.Canny(
        blurred,
        threshold1=low_threshold,
        threshold2=high_threshold
    )
    return edges
