# 🧍 Human Pose Detection & Pose Estimation System

A real-time human pose detection system built using **MediaPipe Pose** and **OpenCV**, designed with clean, modular architecture suitable for industry review, hackathons, and computer vision portfolios.

This project focuses on **clarity, extensibility, and real-time performance**, following production-style software structuring instead of notebook-based experimentation.

---

## 📌 Problem Statement

Human pose estimation is a core building block in applications such as:
- Fitness and exercise tracking
- Posture correction systems
- Sports biomechanics analysis
- AR/VR interaction
- Human–computer interaction

Most beginner implementations tightly couple logic in notebooks, making them hard to scale or maintain.  
This project demonstrates **how pose estimation systems are structured in real-world applications**.

---

## 🧠 Solution Overview

The system uses **MediaPipe Pose** to detect 33 body landmarks in real time and applies geometric analysis to compute joint angles.

### Key Capabilities
- Real-time webcam pose detection
- Landmark visualization
- Joint angle calculation (e.g., elbow, knee)
- Modular, reusable components
- Easily extendable to exercise detection

<img width="640" height="640" alt="image" src="https://github.com/user-attachments/assets/bdb39473-ca5c-4c9c-b638-ebfb16c871fb" />

---

## 📁 Project Structure

```
pose_estimation/
│
├── core/
│   ├── pose_detector.py     # MediaPipe pose wrapper
│   ├── pose_math.py         # Angle & geometry calculations
│
├── viz/
│   └── visualizer.py        # Landmark & angle visualization
│
├── io/
│   └── video_stream.py      # Webcam / video input handling
│
├── main.py                  # Application entry point
├── requirements.txt
└── README.md
```

Each module has a **single responsibility**, reflecting industry best practices.

---

## ⚙️ Pipeline Flow

```
Webcam / Video Stream
        ↓
MediaPipe Pose Detection
        ↓
Landmark Extraction
        ↓
Joint Angle Computation
        ↓
Visualization & Overlay
```

---

## 🧩 Core Components

### 🔹 Pose Detector
- Wraps MediaPipe Pose API
- Handles landmark detection and drawing
- Abstracted for reuse across projects

### 🔹 Pose Math
- Computes angles between joints using vector geometry
- Independent of vision logic (testable & reusable)

### 🔹 Visualization
- Renders landmarks, skeleton, and angle values
- Keeps UI separate from computation

### 🔹 Video Stream
- Handles webcam or video input
- Clean resource management

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Application
```bash
python main.py
```

Press **`Q`** to exit the video stream.

---

## 🛠 Technologies Used

- **Python**
- **MediaPipe** – pose landmark detection
- **OpenCV** – video processing & visualization
- **NumPy** – numerical operations

---

## 📈 Why This Design Works

- ✔ Real-time performance
- ✔ Clean separation of concerns
- ✔ Easily testable components
- ✔ Production-style structure
- ✔ Ready for extension into fitness or AR systems

This structure mirrors how **computer vision pipelines are built in industry**.

---

## 🔮 Future Enhancements

- Exercise detection (squats, push-ups, lunges)
- Rep counting and form validation
- Pose classification using ML models
- Mobile app or REST API integration
- Multi-person pose tracking

---

## 📄 License

Intended for educational, research, and prototype use.

---

### ⭐ Portfolio Note
This project demonstrates **engineering discipline**, not just model usage — a key differentiator in technical interviews.
