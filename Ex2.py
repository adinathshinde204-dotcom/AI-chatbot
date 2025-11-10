import streamlit as st
import google.generativeai as genai
from PIL import Image

# 🔑 Configure your API key
genai.configure("Enter your API key")

# Streamlit App
st.header('Visual Question Answering App')

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file), caption="Uploaded Image")

# Text Input
prompt = st.text_input("Enter the text")

# Button for Response
if st.button("GET RESPONSE"):
    if uploaded_file is not None:
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Use PIL Image directly in the request
        img = Image.open(uploaded_file)

        # Generate Response
        response = model.generate_content([prompt, img])
        st.markdown(response.text)
    else:
        st.warning("⚠️ Please upload an image first!")

