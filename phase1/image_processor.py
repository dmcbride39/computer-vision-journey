import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="DVN VISION", page_icon="📷", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0a0a0a; color: #ffffff; }
    h1 { font-family: 'Helvetica Neue', sans-serif; font-weight: 300; letter-spacing: 6px; font-size: 3.2rem; }
    .subtitle { color: #888888; letter-spacing: 4px; font-size: 1.2rem; }
    .stButton>button { background-color: #1a1a1a; border: 1px solid #444; height: 55px; font-size: 1rem; }
    .stButton>button:hover { background-color: #ffffff; color: black; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>D V N</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">VISION — CINEMATIC IMAGE LAB</p>', unsafe_allow_html=True)
st.markdown("---")

# Session state to remember the last processed image
if 'last_processed' not in st.session_state:
    st.session_state.last_processed = None
if 'last_effect' not in st.session_state:
    st.session_state.last_effect = "Original"

uploaded_file = st.file_uploader("DROP IMAGE TO BEGIN", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    if len(img_array.shape) == 3:
        original = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    else:
        original = img_array

    tab1, tab2 = st.tabs(["📸 ORIGINAL", "🎬 PROCESSED"])

    with tab1:
        st.image(image, use_container_width=True)

    with tab2:
        st.subheader("Cinematic Studio Effects")

        cols = st.columns(4)

        with cols[0]:
            if st.button("MONOCHROME"):
                result = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                st.image(result, use_container_width=True, channels="GRAY")
                st.session_state.last_processed = result
                st.session_state.last_effect = "Monochrome"

        with cols[1]:
            if st.button("SOFT BOKEH"):
                result = cv2.GaussianBlur(original, (51, 51), 0)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.session_state.last_processed = result
                st.session_state.last_effect = "Soft Bokeh"

        with cols[2]:
            if st.button("CINEMATIC BARS"):
                h, w = original.shape[:2]
                bar = int(h * 0.15)
                result = original.copy()
                result[0:bar] = 0
                result[h-bar:h] = 0
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.session_state.last_processed = result
                st.session_state.last_effect = "Cinematic Bars"

        with cols[3]:
            if st.button("PREMIUM SHARPEN"):
                kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                result = cv2.filter2D(original, -1, kernel)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.session_state.last_processed = result
                st.session_state.last_effect = "Premium Sharpen"

        # Advanced Tools
        st.markdown("### Advanced Cinematic Tools")
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            if st.button("VINTAGE 35mm FILM"):
                warm = cv2.convertScaleAbs(original, alpha=1.25, beta=15)
                bright = cv2.threshold(cv2.cvtColor(warm, cv2.COLOR_BGR2GRAY), 200, 255, cv2.THRESH_BINARY)[1]
                glow = cv2.GaussianBlur(bright, (35, 35), 0)
                glow = cv2.cvtColor(glow, cv2.COLOR_GRAY2BGR)
                result = cv2.addWeighted(warm, 0.85, glow, 0.6, 10)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.session_state.last_processed = result
                st.session_state.last_effect = "Vintage 35mm"

        with col_b:
            if st.button("ANAMORPHIC FLARE"):
                gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                _, bright = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
                flare = cv2.GaussianBlur(bright, (101, 21), 0)
                flare = cv2.cvtColor(flare, cv2.COLOR_GRAY2BGR)
                result = cv2.addWeighted(original, 0.75, flare, 0.8, 30)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.session_state.last_processed = result
                st.session_state.last_effect = "Anamorphic Flare"

        with col_c:
            if st.button("DRAMATIC CONTRAST"):
                result = cv2.convertScaleAbs(original, alpha=1.9, beta=-25)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), use_container_width=True)
                st.session_state.last_processed = result
                st.session_state.last_effect = "Dramatic Contrast"

    # ================== SAVE PROCESSED IMAGE ==================
    st.markdown("---")
    if st.session_state.last_processed is not None:
        if st.button(f"💾 SAVE {st.session_state.last_effect.upper()} IMAGE"):
            buf = io.BytesIO()
            if len(st.session_state.last_processed.shape) == 2:  # Grayscale
                processed_pil = Image.fromarray(st.session_state.last_processed)
            else:
                processed_pil = Image.fromarray(cv2.cvtColor(st.session_state.last_processed, cv2.COLOR_BGR2RGB))
            processed_pil.save(buf, format="PNG")
            st.download_button(
                label="Download Processed Image",
                data=buf.getvalue(),
                file_name=f"DVN_{st.session_state.last_effect.replace(' ', '_')}.png",
                mime="image/png"
            )
    else:
        st.info("Apply an effect first, then save.")