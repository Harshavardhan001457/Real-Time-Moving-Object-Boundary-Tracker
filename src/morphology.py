import cv2
import numpy as np


def stabilize_edges(edge_frame: np.ndarray, kernel_size: int = 5, iterations: int = 2):

    if edge_frame is None:
        raise ValueError("stabilize_edges received None input")

    if len(edge_frame.shape) != 2:
        raise ValueError("stabilize_edges expects a single-channel image")

    # Structuring the element
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (kernel_size, kernel_size)
    )

    #Close small gaps in edges
    closed = cv2.morphologyEx(
        edge_frame,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=iterations
    )

    #Dilate to strengthen edge connections
    dilated = cv2.dilate(
        closed,
        kernel,
        iterations=1
    )

    #Erode slightly to reduce thickness
    stabilized = cv2.erode(
        dilated,
        kernel,
        iterations=1
    )
    return stabilized
