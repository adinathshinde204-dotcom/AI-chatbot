# import streamlit as st
# import google.generativeai as genai
# from PIL import Image
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # Configure API key
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.header("Visual Question Answering App")

# uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     img = Image.open(uploaded_file)
#     st.image(img, caption="Uploaded Image")

# prompt = st.text_input("Enter the question")

# if st.button("GET RESPONSE"):
#     if uploaded_file and prompt:
#         model = genai.GenerativeModel("gemini-2.5-flash")
#         response = model.generate_content([prompt, img])
#         st.markdown(response.text)
#     else:
#         st.warning("⚠️ Upload image & enter question")

















import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="VisionAI • Visual Q&A",
    page_icon="✨",
    layout="wide"
)

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
/* Background */
.main {
    background: radial-gradient(circle at top, #020617, #000000);
    color: white;
}

/* Hero */
.hero {
    padding: 40px 20px 10px 20px;
    text-align: center;
}
.hero h1 {
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg,#38bdf8,#22c55e,#a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    font-size: 18px;
    color: #cbd5e1;
    max-width: 700px;
    margin: auto;
}

/* Glass Card */
.glass {
    background: rgba(2, 6, 23, 0.7);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(148, 163, 184, 0.15);
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#22c55e,#38bdf8);
    color: #020617;
    font-weight: 700;
    border-radius: 14px;
    height: 52px;
    font-size: 17px;
}

/* Inputs */
.stTextInput>div>div>input {
    border-radius: 14px;
    height: 50px;
    font-size: 16px;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HERO ------------------
st.markdown("""
<div class="hero">
    <h1>✨ VisionAI</h1>
    <p>Upload an image and ask intelligent questions.  
    Powered by <b>Google Gemini Vision</b> for instant visual understanding.</p>
</div>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.markdown("## 🚀 VisionAI")
    st.write("AI-powered Visual Question Answering platform.")
    st.markdown("---")
    st.markdown("### 🧠 Capabilities")
    st.markdown("- Image understanding")
    st.markdown("- Scene explanation")
    st.markdown("- Object detection")
    st.markdown("- Contextual reasoning")
    st.markdown("---")
    st.markdown("👨‍💻 **Developer**  \nAdinath Shinde")

# ------------------ MAIN LAYOUT ------------------
left, right = st.columns([1, 1], gap="large")

# ---------- LEFT: IMAGE ----------
with left:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 📤 Upload Image")

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["png", "jpg", "jpeg"]
    )

    image = None
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- RIGHT: QUESTION & ANSWER ----------
with right:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 💬 Ask a Question")

    prompt = st.text_input(
        "Your question",
        placeholder="What is happening in this image?"
    )

    if st.button("✨ Generate Answer"):
        if image and prompt:
            with st.spinner("Analyzing image with AI..."):
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content([prompt, image])

                st.markdown("### 🤖 AI Response")
                st.write(response.text)
        else:
            st.warning("Please upload an image and enter a question.")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
    © 2025 VisionAI • Built with Streamlit & Google Gemini
</div>
""", unsafe_allow_html=True)
