import cv2
import numpy as np


def isolate_moving_object(stabilized_edges: np.ndarray, min_area: int = 3000):
    if stabilized_edges is None:
        raise ValueError("isolate_moving_object received None input")

    # Find the contours from stabilized edge map
    contours, _ = cv2.findContours(
        stabilized_edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    # Create empty mask
    object_mask = np.zeros_like(stabilized_edges)

    if not contours:
        return object_mask

    # Select the largest contour by area
    largest_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest_contour)

    # Filter small noisy contours
    if area < min_area:
        return object_mask

    # Fill the contour to create solid object mask
    cv2.drawContours(
        object_mask,
        [largest_contour],
        contourIdx=-1,
        color=255,
        thickness=cv2.FILLED
    )
    return object_mask