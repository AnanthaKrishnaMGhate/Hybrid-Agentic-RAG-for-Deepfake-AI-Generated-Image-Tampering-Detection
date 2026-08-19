import streamlit as st
import json
import easyocr
from PIL import Image

from rag.rag_pipeline import run_rag

# ====================================
# PAGE SETTINGS
# ====================================

st.set_page_config(
    page_title="Fake News Detection System",
    page_icon="📰",
    layout="wide"
)

# ====================================
# OCR READER
# ====================================

reader = easyocr.Reader(['en'])

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("📰 Project Information")

st.sidebar.markdown("### Vector Database")
st.sidebar.success("FAISS")

st.sidebar.markdown("### LLM")
st.sidebar.success("Groq Llama 3.3")

st.sidebar.markdown("### Sources Used")

sources = [
    "Kaggle Dataset",
    "Wikipedia API",
    "NewsAPI",
    "GDELT API",
    "Currents API",
    "Mediastack API",
    "Alpha Vantage API",
    "New York Times API",
    "Guardian API",
    "TheNewsAPI",
    "World News API",
    "RSS Feeds",
    "News Channel Scraping"
]

for source in sources:
    st.sidebar.write("✅", source)

# ====================================
# TITLE
# ====================================

st.title("📰 Fake News Detection using RAG + Groq")

st.markdown(
"""
Detect whether news is **REAL** or **FAKE**
using:

- RAG
- FAISS
- Multiple News APIs
- RSS Feeds
- Web Scraping
- Groq LLM
"""
)

st.divider()

# ====================================
# INPUT AREA
# ====================================

left, right = st.columns([2, 1])

with left:

    news_text = st.text_area(
        "Paste News Content",
        height=250
    )

with right:

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

# ====================================
# IMAGE OCR
# ====================================

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    result = reader.readtext(image)

    extracted_text = ""

    for item in result:

        extracted_text += item[1] + " "

    st.subheader("Extracted Text")

    st.info(extracted_text)

    if news_text.strip() == "":

        news_text = extracted_text

# ====================================
# ANALYZE BUTTON
# ====================================

if st.button("🔍 Analyze News"):

    if news_text.strip() == "":

        st.warning("Please enter text or upload image.")

    else:

        with st.spinner("Analyzing..."):

            response = run_rag(news_text)

        # -----------------------------------
        # Remove markdown formatting
        # -----------------------------------

        response = response.replace("```json", "")
        response = response.replace("```", "")

        try:

            data = json.loads(response)

            prediction = data.get("prediction", "Unknown")
            confidence = data.get("confidence", "Unknown")
            reason = data.get("reason", "")

        except:

            prediction = "Unknown"
            confidence = "Unknown"
            reason = response

        # ====================================
        # CATEGORY DETECTION
        # ====================================

        text_lower = news_text.lower()

        category = "General"

        if any(x in text_lower for x in
               ["election", "minister", "government", "cm", "pm"]):

            category = "Politics"

        elif any(x in text_lower for x in
                 ["cricket", "football", "ipl", "match"]):

            category = "Sports"

        elif any(x in text_lower for x in
                 ["ai", "technology", "robot", "computer"]):

            category = "Technology"

        elif any(x in text_lower for x in
                 ["movie", "actor", "cinema"]):

            category = "Entertainment"

        elif any(x in text_lower for x in
                 ["hospital", "covid", "disease"]):

            category = "Health"

        elif any(x in text_lower for x in
                 ["market", "business", "stock"]):

            category = "Business"

        elif any(x in text_lower for x in
                 ["nasa", "isro", "space"]):

            category = "Science"

        elif any(x in text_lower for x in
                 ["army", "defence", "missile"]):

            category = "Defence"

        # ====================================
        # NEWS TYPE
        # ====================================

        news_type = "International"

        if "india" in text_lower:

            news_type = "National"

        if any(x in text_lower for x in
               ["karnataka", "bangalore", "mysore"]):

            news_type = "Regional"

        # ====================================
        # RESULT CARD
        # ====================================

        st.divider()

        if prediction.upper() == "REAL":

            st.success("✅ REAL NEWS")

        elif prediction.upper() == "FAKE":

            st.error("❌ FAKE NEWS")

        else:

            st.warning("⚠ Unable to determine")

        # ====================================
        # DETAILS
        # ====================================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Confidence")

            st.info(confidence)

            st.subheader("Category")

            st.info(category)

        with col2:

            st.subheader("News Type")

            st.info(news_type)

            if news_type == "Regional":

                region = "State / Regional"

            elif news_type == "National":

                region = "India"

            else:

                region = "International"

            st.subheader("Region")

            st.info(region)

        # ====================================
        # SOURCES
        # ====================================

        st.subheader("Sources Used")

        source_col1, source_col2 = st.columns(2)

        with source_col1:

            st.write("✅ FAISS Dataset")
            st.write("✅ Wikipedia")
            st.write("✅ NewsAPI")
            st.write("✅ GDELT")
            st.write("✅ Currents")
            st.write("✅ Mediastack")
            st.write("✅ Alpha Vantage")

        with source_col2:

            st.write("✅ New York Times")
            st.write("✅ Guardian")
            st.write("✅ TheNewsAPI")
            st.write("✅ World News API")
            st.write("✅ RSS Feeds")
            st.write("✅ News Scraper")

        # ====================================
        # EXPLANATION
        # ====================================

        with st.expander("Detailed Explanation"):

            st.write(reason)