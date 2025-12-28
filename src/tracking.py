from collections import deque

# Tracks centroid positions across frames to form a trajectory.
class CentroidTracker:
    def __init__(self, max_length: int = 50):
        self.trajectory = deque(maxlen=max_length)

    def update(self, centroid):
        if centroid is not None:
            self.trajectory.append(centroid)

    def get_trajectory(self):
        return list(self.trajectory)

    def reset(self):
        self.trajectory.clear() # Clear trajectory history.
