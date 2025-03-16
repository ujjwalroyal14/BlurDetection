import streamlit as st
import numpy as np
from PIL import Image
import cv2
import glob
images_folder = "images"  
threshold = 50.0       

st.title('BlurDetection')
uploaded_files = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
print(len(uploaded_files))
for i in uploaded_files:
   
    img=Image.open(i)
    image=np.array(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    edges = cv2.Canny(gray, 100, 200)
    edge_count = cv2.countNonZero(edges)
    text = "Not Blurry"
    if fm < threshold or edge_count < 5000:  # Adjust edge_count threshold as needed
        text = "Blurry"
    st.write(text)
    st.image(img)
   
