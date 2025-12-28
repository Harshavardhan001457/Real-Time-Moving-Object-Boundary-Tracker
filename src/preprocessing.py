import cv2
import numpy as np


def preprocess_frame( frame: np.ndarray, resize_width: int = 640):
    if frame is None:
        raise ValueError("preprocess_frame received None input")

    # Resize while maintaining aspect ratio
    h, w = frame.shape[:2]
    scale = resize_width / float(w)
    new_dim = (resize_width, int(h * scale))
    resized = cv2.resize(frame, new_dim)

    # Convert to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Light blur to suppress noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    return gray
