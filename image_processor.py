import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("🖼️ My First Image Processor")
st.write("**Devin's Computer Vision Project**")

# Upload image
uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    # Convert to OpenCV format
    if len(img_array.shape) == 3:
        original = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    else:
        original = img_array

    st.image(image, caption="Original Photo", use_column_width=True)

    # Buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Make Black & White"):
            gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            st.image(gray, caption="Black & White", use_column_width=True, channels="GRAY")

    with col2:
        if st.button("Blur Image"):
            blurred = cv2.GaussianBlur(original, (25, 25), 0)
            st.image(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB), caption="Blurred", use_column_width=True)

    with col3:
        if st.button("Find Edges"):
            gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            st.image(edges, caption="Edges Detected", use_column_width=True, channels="GRAY")

    # Extra option
    if st.button("Resize Image (Small)"):
        small = cv2.resize(original, (400, 300))
        st.image(cv2.cvtColor(small, cv2.COLOR_BGR2RGB), caption="Resized Image", use_column_width=True)