import cv2
import streamlit as st

def main():
    st.title("SATELLITE IMAGE STITCHING")

    st.header("Upload your images")
    uploaded_files = st.file_uploader("", accept_multiple_files=True)

    image_paths = []
    if uploaded_files is not None:
        for file in uploaded_files:
            image_paths.append(file.name)
            with open(file.name, "wb") as f:
                f.write(file.getbuffer())

    if len(image_paths) < 2:
        st.warning("Please upload at least two images to perform image stitching.")
        return

    # Load and resize images
    imgs = []
    for i in range(len(image_paths)):
        img = cv2.imread(image_paths[i])
        img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
        imgs.append(img)

    # Show original pictures
    st.subheader("Unstitched Images:")
    cols = st.columns(len(image_paths))
    
    # Display each image in a separate column
    for i, col in enumerate(cols):
        col.image(image_paths[i], use_column_width=True, caption=f"Image {i+1}")

    stitcher = cv2.Stitcher.create()
    status, output = stitcher.stitch(imgs)

    if status != cv2.Stitcher_OK:
        # Checking if the stitching procedure is successful
        st.error("Stitching was unsuccessful.")
    else:
        # Display final output
        st.subheader("Final Image:")
        st.image(output, channels="BGR")
        st.success("Successfully Stitched the image!!!")

if __name__ == "__main__":
    main()
