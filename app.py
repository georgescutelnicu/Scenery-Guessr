import streamlit as st
from PIL import Image
import random
import os


st.set_page_config(page_title="Scenery Guessr",
                   page_icon=":globe_with_meridians:",
                   layout="wide")
st.markdown(
    """
    <style>
        .stMainBlockContainer {
            width: 60%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Scenery Guessr")
st.markdown("Practice recognizing sceneries and sharpen your GeoGuessr skills.")

image_folder = "./data"
image_files = os.listdir(image_folder)

if "current_image" not in st.session_state:
    st.session_state.current_image = None
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if st.button("Display a random image"):
    st.session_state.current_image = random.choice(image_files)
    st.session_state.show_answer = False

if st.button("Display answer"):
    st.session_state.show_answer = True

st.markdown("---")

if st.session_state.current_image:
    image = Image.open(os.path.join(image_folder, st.session_state.current_image))
    st.image(image)

if st.session_state.show_answer and st.session_state.current_image:
    image_name = st.session_state.current_image.split(".")[0].replace("_", " ")[:-1].upper()
    st.markdown(f"{image_name}")
