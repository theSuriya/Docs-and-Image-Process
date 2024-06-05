import streamlit as st
from image_process import Image_Response
from model import AllModel
from pdf_process import PdfExtract
import PIL.Image
import io

# Custom title with adjustable size and styling
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 28px;
        color: white;
    }
    .subheader {
        font-size: 20px;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>Document and Image Processing App</h1>", unsafe_allow_html=True)

# Sidebar for file upload and options
with st.sidebar:
    st.subheader("Upload File")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])
    st.subheader("Select Processing Options")
    summarize = st.checkbox("Summarize")
    translate = st.checkbox("Translate to language")
    extract_keywords = st.checkbox("Extract Keywords")
    sentiment_analysis = st.checkbox("Analyze Sentiment")

    st.markdown("<h2 class='subheader'>About</h2>", unsafe_allow_html=True)
    st.caption("""
    This app allows you to upload and process documents and images. 
    You can perform various operations like summarizing text, translating to different languages, 
    extracting keywords, and analyzing sentiment. 
    Simply upload a file and select the desired options to get started.
    """)

    st.subheader("Build By:")
    st.write("[Suriya❤️](https://github.com/theSuriya)")
    st.write("contact: [Email](mailto:thesuriya3@gamil.com)")

# Initialize the model
all_model = AllModel()

# Main content
if uploaded_file is not None:
    # Read the file as bytes
    file_bytes = io.BytesIO(uploaded_file.getvalue())

    # Attempt to open the file as an image
    try:
        img = PIL.Image.open(file_bytes)
        st.markdown("<h2 class='subheader'>Image Column</h2>", unsafe_allow_html=True)
        st.image(uploaded_file)
        input = st.text_input('Ask any question related to the image')
        submit = st.button('Generate')
        if submit and input:
            response = Image_Response(input, uploaded_file)
            st.write(response.output)

    except Exception as e:
        # If the file is not an image, treat it as a document
        st.markdown("<h2 class='subheader'>Document uploaded</h2>", unsafe_allow_html=True)
        pdf_text = PdfExtract(file_bytes)
        col1, col2 = st.columns(2)

        if summarize:
            with col1:
                st.success('Summary of the given document:')
                response = all_model.summarize(pdf_text.extracted_text)
                st.write(response)

        if translate:
            with col2:
                st.success('Translated Document:')
                lan = st.text_input('Which language would you like to translate the document to?')
                submit = st.button('generate')
                if lan and submit:
                    response = all_model.translate(pdf_text.extracted_text, lan)
                    st.write(response)

        if extract_keywords:
            with col1:
                st.success('Extracted Keywords:')
                response = all_model.extract_keywords(pdf_text.extracted_text)
                st.write(response)

        if sentiment_analysis:
            with col2:
                st.success('Sentiment Analysis:')
                response = all_model.sentiment_analysis(pdf_text.extracted_text)
                st.write(response)
else:
    st.markdown("<h2 class='subheader'>Please upload a file to get started.</h2>", unsafe_allow_html=True)
