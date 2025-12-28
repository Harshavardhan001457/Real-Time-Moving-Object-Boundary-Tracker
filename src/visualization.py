import cv2

# Draw contour, bounding box, convex hull, and centroid trajectory.
def draw_visuals( frame, geometry: dict, trajectory: list):
    if geometry is None:
        return frame

    # Draw contour
    cv2.drawContours(frame, [geometry["contour"]], -1, (0, 255, 0), 2)

    # Draw bounding box
    x, y, w, h = geometry["bounding_box"]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Draw convex hull
    cv2.drawContours(frame, [geometry["convex_hull"]], -1, (0, 0, 255), 2)

    # Draw centroid
    cx, cy = geometry["centroid"]
    cv2.circle(frame, (cx, cy), 5, (0, 255, 255), -1)

    # Draw centroid trajectory
    for i in range(1, len(trajectory)):
        cv2.line(frame, trajectory[i - 1], trajectory[i], (255, 255, 0),2)

    return frame
