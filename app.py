import streamlit as st
import numpy as np
import requests
from PIL import Image
from io import BytesIO
st.title("Image Uploader")
uploaded_image = st.file_uploader("Upload a JPG", type=["jpg"])
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    response = requests.post("https://docker-auto-ai-bluesky-ku6cxn3xga-ew.a.run.app", files={"file": uploaded_image})
# Check if the request was successful
    if response.status_code == 200:
        # Read the image data from the response
        image_bytes = BytesIO(response.content)
        # Open the image using Pillow (PIL)
        img = Image.open(image_bytes)
        # Display the image in Streamlit
        st.image(img, caption='Image Caption', use_column_width=True)
    else:
        st.error('Failed to fetch image. Status code: {}'.format(response.status_code))
