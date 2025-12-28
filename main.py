import cv2

from src.video_stream import VideoStream
from src.preprocessing import preprocess_frame
from src.edge_detection import detect_edges
from src.morphology import stabilize_edges
from src.object_isolation import isolate_moving_object
from src.contours import extract_object_geometry
from src.tracking import CentroidTracker
from src.visualization import draw_visuals


def main():
    # Initialize video stream
    video = VideoStream(src=0, width=640, height=480)

    # Initialize centroid tracker
    tracker = CentroidTracker(max_length=50)

    print("[INFO] Press 'q' to exit")

    while True:
        frame = video.read()
        if frame is None:
            break

        # 1. Preprocessing
        gray = preprocess_frame(frame)

        # 2. Edge detection
        edges = detect_edges(gray)

        # 3. Edge stabilization
        stabilized = stabilize_edges(edges)

        # 4. Object isolation
        object_mask = isolate_moving_object(stabilized)

        # 5. Geometry extraction
        geometry = extract_object_geometry(object_mask)

        # 6. Tracking
        if geometry is not None:
            tracker.update(geometry["centroid"])
        else:
            tracker.update(None)

        # 7. Visualization
        annotated = draw_visuals(
            frame,
            geometry,
            tracker.get_trajectory()
        )

        # Display result
        cv2.imshow("Moving Object Boundary Tracker", annotated)

        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
