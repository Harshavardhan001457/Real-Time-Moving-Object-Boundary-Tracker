import cv2
import numpy as np


def extract_object_geometry(object_mask: np.ndarray):
    if object_mask is None:
        raise ValueError("extract_object_geometry received None input")
    contours, _ = cv2.findContours(
        object_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    if not contours:
        return None
    # Take the Largest contour (dominant object)
    contour = max(contours, key=cv2.contourArea)

    if cv2.contourArea(contour) == 0:
        return None
    # Bounding box
    x, y, w, h = cv2.boundingRect(contour)

    # Convex hull
    hull = cv2.convexHull(contour)

    # Centroid (using image moments)
    M = cv2.moments(contour)
    if M["m00"] == 0:
        return None

    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    return {
        "contour": contour,
        "bounding_box": (x, y, w, h),
        "convex_hull": hull,
        "centroid": (cx, cy)
    }
