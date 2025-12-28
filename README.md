# Real-Time Moving Object Boundary Tracker (Classical OpenCV)

##  Introduction

This repository contains a **real-time motion-based object boundary tracking system** built using **classical computer vision techniques** in OpenCV.
The system processes a live webcam feed to detect and track the **boundary and movement** of a moving object (e.g., a hand) without using any deep learning models or high-level tracking APIs.

The focus of this project is to demonstrate **fundamental computer vision reasoning**, including edge detection, morphological processing, contour analysis, and motion tracking.

---

## Core Logic & Approach

### Key Idea

Instead of recognizing *what* the object is, the system focuses on **how the object moves and how its boundaries evolve over time**.

> A moving object produces **consistent, dominant edge structures** across consecutive frames, while the background remains comparatively static.

By exploiting this property, the system can isolate and track a moving object using only classical image processing.

---

## Processing Pipeline (How It Works)

The system follows a **strict sequential pipeline**, executed on every video frame:

### 1️ Frame Acquisition

* Capture frames from the webcam in real time.
* Resize frames for consistent and efficient processing.

### 2 Preprocessing

* Convert frames to grayscale (color is not required for boundary detection).
* Apply Gaussian blur to reduce sensor noise and minor intensity fluctuations.

### 3️ Edge Detection (Canny)

* Use the Canny Edge Detector to highlight strong intensity gradients.
* This step extracts **potential object boundaries** but may produce fragmented edges.

### 4️ Edge Stabilization (Morphological Operations)

* Apply morphological **closing** to connect broken edge segments.
* Use dilation and erosion to strengthen object boundaries and suppress noise.
* This step stabilizes the perceived shape of the moving object.

### 5️ Object Isolation

* Detect all contours in the stabilized edge map.
* Select the **largest contour by area**, assuming it corresponds to the dominant moving object.
* Generate a binary mask representing only the moving object.

### 6️ Geometry Extraction

From the isolated object mask:

* Extract the **primary contour**
* Compute the **bounding box**
* Compute the **convex hull**
* Calculate the **centroid** using image moments

### 7️ Motion Tracking

* Track the centroid position across frames.
* Store centroid history in a fixed-length buffer.
* Use this history to represent the object’s **movement trajectory**.

### 8️ Visualization

Draw the following on the original video frame:

* Object contour
* Bounding box
* Convex hull
* Centroid trajectory (motion path)

---

## Visual Output

The live video feed displays:

* 🟢 Contour of the moving object
* 🔵 Bounding box enclosing the object
* 🔴 Convex hull outlining the outer shape
* 🟡 Trajectory showing the object’s movement over time

These visualizations provide an intuitive understanding of both **object shape** and **motion dynamics**.

---

##  Technologies Used

* **Python**
* **OpenCV**
* **NumPy**

⚠️ No deep learning
⚠️ No MediaPipe
⚠️ No pre-trained models
⚠️ No high-level trackers (KCF, CSRT, etc.)

---

##  Project Structure

```
moving-object-boundary-tracker/
│
├── main.py                     # Pipeline execution and application entry point
│
├── src/
│   ├── video_stream.py         # Webcam capture handling
│   ├── preprocessing.py        # Frame preprocessing
│   ├── edge_detection.py       # Canny edge detection
│   ├── morphology.py           # Edge stabilization
│   ├── object_isolation.py     # Dominant object extraction
│   ├── contours.py             # Geometry computation
│   ├── tracking.py             # Centroid tracking logic
│   └── visualization.py        # Drawing and visualization
│
├── demo/
│   ├── demo_video.mp4          # Demo screen Recording
│
├── requirements.txt
└── README.md
```

---

##  What We Implemented in This Project

* A complete **classical computer vision pipeline**
* Real-time webcam processing
* Edge-based object boundary detection
* Morphology-based edge stabilization
* Dominant moving object isolation
* Geometric analysis (contour, hull, bounding box)
* Motion tracking using centroid history
* Clean, modular, and explainable code structure

---

##  How to Run

```bash
pip install opencv-python numpy
python main.py
```

Press **`q`** to exit the application.

---

##  Learning Outcomes

This project strengthens understanding of:

* Classical computer vision fundamentals
* Edge detection and morphology
* Contour-based object representation
* Geometric feature extraction
* Motion tracking using temporal data
* Real-time vision pipeline design

---

##  Limitations & Notes

This system is based on an **edge-driven classical computer vision pipeline**.  
As a result, its performance depends on the presence of sufficient **intensity gradients** between the moving object and the background.

- On **textured or cluttered backgrounds** (doors, boxes, furniture, irregular surfaces), the system performs reliably due to strong edge contrast.
- On **plain or uniform backgrounds** (single-colored walls or smooth surfaces), object detection may fail because very few edges are generated by the Canny edge detector.

This behavior is an **expected limitation** of edge-based pipelines and not an implementation error.  
The limitation can be addressed by integrating **motion-based background subtraction techniques** (e.g., MOG2), which were intentionally not included to keep the pipeline purely edge-based and aligned with classical OpenCV fundamentals.

---

##  Final Note

This project demonstrates that **robust real-time object tracking can be achieved without deep learning**, using well-designed classical computer vision techniques.
It serves as a strong foundation for further exploration into advanced tracking, robotics perception, and autonomous systems.