import cv2
import streamlit as st

def main():
    st.title("Satellite Image Stitching")

    st.write("Upload your images")
    uploaded_files = st.file_uploader("", accept_multiple_files=True)
    image_paths = []
    if uploaded_files is not None:
        for file in uploaded_files:
            image_paths.append(file.name)
            with open(file.name, "wb") as f:
                f.write(file.getbuffer())

    # Load and resize images
    imgs = []
    for i in range(len(image_paths)):
        img = cv2.imread(image_paths[i])
        img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
        imgs.append(img)
