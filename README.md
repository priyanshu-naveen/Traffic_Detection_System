# Traffic_Detection_System

# 🚗 Traffic Detection System

A real-time **vehicle detection and counting system** built using **YOLO, OpenCV, PyTorch, and Streamlit**. The application can detect vehicles from images, videos, and a live mobile camera feed through an easy-to-use web interface.

## ✨ Features

* 🚘 **Vehicle Detection** using a trained YOLO model
* 📷 **Image Detection** – Upload an image and detect vehicles
* 🎥 **Video Detection** – Upload a video for frame-by-frame vehicle detection
* 📱 **Mobile Camera Detection** – Use a phone camera directly through the browser
* 🔢 **Vehicle Counting** – Displays the number of detected vehicles in images
* ⚙️ **Confidence Threshold** – Adjust detection confidence from the sidebar
* 🌐 **Streamlit Web Interface** – Simple and interactive UI
* 🐳 **Docker Support** – Includes a Dockerfile for containerized deployment
* 💻 **CPU Support** – Configured to run on CPU-based environments such as Streamlit Cloud

## 🛠️ Tech Stack

* **Python**
* **YOLO / Ultralytics**
* **OpenCV**
* **PyTorch**
* **Streamlit**
* **Streamlit-WebRTC**
* **NumPy**
* **Pillow**
* **AV**

## 📂 Project Structure

```text
Traffic_Detection_System/
│
├── ui.py              # Main Streamlit application
├── best.pt            # Trained YOLO model
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
└── README.md          # Project documentation
```

## ⚙️ How It Works

The application loads the trained YOLO model from `best.pt` and uses it to process the selected input.

```text
Input
  │
  ├── Image
  ├── Video
  └── Mobile Camera
        │
        ▼
   YOLO Model
        │
        ▼
 Vehicle Detection
        │
        ├── Bounding Boxes
        └── Vehicle Counts
        │
        ▼
 Streamlit Interface
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/priyanshu-naveen/Traffic_Detection_System.git
cd Traffic_Detection_System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run ui.py
```

The application will open in your browser.

## 📷 Using the Application

### Image Mode

1. Select **Image** from the sidebar.
2. Upload a `.jpg`, `.jpeg`, or `.png` image.
3. The YOLO model detects vehicles.
4. Detected vehicles are displayed with bounding boxes.
5. The application displays the detected vehicle count.

### 🎥 Video Mode

1. Select **Video** from the sidebar.
2. Upload an `.mp4`, `.avi`, or `.mov` video.
3. The application processes the video frames.
4. Detected vehicles are displayed in the Streamlit interface.

### 📱 Mobile Camera Mode

1. Select **Mobile Camera**.
2. Open the application on a device with a camera.
3. Allow camera access when requested.
4. The system performs real-time vehicle detection using the camera feed.

## ⚙️ Confidence Threshold

The sidebar provides a **Confidence Threshold** slider.

A higher value produces more selective detections, while a lower value can detect more objects but may also produce false detections.

Default value:

```text
0.40
```

## 🧠 Model

The project uses a trained YOLO model stored as:

```text
best.pt
```

The model is loaded using the Ultralytics YOLO framework.

```python
from ultralytics import YOLO

model = YOLO("best.pt")
```

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t traffic-detection-system .
```

Run the container:

```bash
docker run -p 8501:8501 traffic-detection-system
```

Then open:

```text
http://localhost:8501
```

## 📦 Dependencies

The project uses the following major dependencies:

```text
streamlit
ultralytics
opencv-python-headless
numpy
pillow
torch
streamlit-webrtc
av
```

The exact versions are specified in `requirements.txt`.

## 🎯 Applications

This system can be used as a foundation for:

* Smart traffic monitoring
* Vehicle counting
* Traffic surveillance
* Road monitoring systems
* Intelligent transportation systems
* Real-time traffic analysis
* Computer vision-based traffic management

## 🔮 Future Improvements

* 🚦 Traffic density estimation
* 🚗 Vehicle tracking across frames
* 📊 Traffic analytics dashboard
* 🛣️ Lane-wise vehicle counting
* 🚨 Accident detection
* 🚥 Traffic violation detection
* 📈 Historical traffic statistics
* ⚡ GPU acceleration for faster inference

## 👨‍💻 Author

**Priyanshu Naveen**

GitHub: [@priyanshu-naveen](https://github.com/priyanshu-naveen)

## 📄 License

This project is available for educational and research purposes.
