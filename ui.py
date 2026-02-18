import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile
from collections import Counter
import torch
import time
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Vehicle Detection System",
    page_icon="🚗",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    from ultralytics import YOLO
    return YOLO("best.pt")


DEVICE = "cpu"   # Streamlit cloud runs on CPU

# ---------------- VEHICLE COUNT FUNCTION ----------------
def count_vehicles(results):
    if results[0].boxes is None:
        return {}

    class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
    class_names = [model.names[i] for i in class_ids]

    return dict(Counter(class_names))

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>🚗 Vehicle Detection System</h1>
    <p style='text-align:center;'>Live Traffic Detection using YOLO</p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Settings")

conf_threshold = st.sidebar.slider(
    "Confidence Threshold",
    0.1, 1.0, 0.4, 0.05
)

source_type = st.sidebar.radio(
    "Select Input Type",
    ("Image", "Video", "Mobile Camera")
)

# =====================================================
# IMAGE
# =====================================================
if source_type == "Image":
    uploaded_image = st.file_uploader(
        "📷 Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:
        image = Image.open(uploaded_image).convert("RGB")
        img_array = np.array(image)

        results = model.predict(
            img_array,
            conf=conf_threshold,
            imgsz=320,
            device=DEVICE
        )

        annotated = results[0].plot()
        vehicle_counts = count_vehicles(results)

        col1, col2 = st.columns([3, 1])

        with col1:
            st.image(annotated, use_container_width=True)

        with col2:
            st.subheader("🚘 Vehicle Count")
            for cls, count in vehicle_counts.items():
                st.write(f"{cls.capitalize()} : {count}")

# =====================================================
# VIDEO
# =====================================================
elif source_type == "Video":
    uploaded_video = st.file_uploader(
        "🎥 Upload Video",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            if frame_count % 3 != 0:
                continue

            results = model.predict(
                frame,
                conf=conf_threshold,
                imgsz=320,
                device=DEVICE
            )

            annotated = results[0].plot()
            annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            stframe.image(annotated, use_container_width=True)

        cap.release()

# =====================================================
# MOBILE CAMERA (REAL PHONE CAMERA)
# =====================================================
elif source_type == "Mobile Camera":

    st.info("Allow camera access in your browser")

    RTC_CONFIGURATION = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )

    class VideoProcessor(VideoProcessorBase):

        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")

            results = model.predict(
                img,
                conf=conf_threshold,
                imgsz=320,
                device=DEVICE
            )

            annotated = results[0].plot()

            return av.VideoFrame.from_ndarray(annotated, format="bgr24")

    webrtc_streamer(
        key="vehicle-detection",
        video_processor_factory=VideoProcessor,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )

# ---------------- FOOTER ----------------
st.markdown(
    """
    <hr>
    <p style='text-align:center;'>
    Built with ❤️ using Streamlit & YOLO
    </p>
    """,
    unsafe_allow_html=True
)

