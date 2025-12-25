import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.header("Visual Question Answering App")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image")

prompt = st.text_input("Enter the question")

if st.button("GET RESPONSE"):
    if uploaded_file and prompt:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content([prompt, img])
        st.markdown(response.text)
    else:
        st.warning("⚠️ Upload image & enter question")
