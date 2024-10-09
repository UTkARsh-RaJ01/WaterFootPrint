import streamlit as st
import pandas as pd
import importlib
import base64
from googletrans import Translator
from PIL import Image
import importlib

def run():
   
    translator = Translator()

    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    
    gif_path = "back3.gif"  

    
    base64_gif = get_base64_of_bin_file(gif_path)

    
    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/gif;base64,{base64_gif}");
        background-size: cover;
        background-position: center;
    }}

    .black-text {{
        color: black;
        margin-left: 480px;
    }}

    .custom-heading {{
        color: black;
        margin-left: 480px;
        font-size: 35px;
    }}
    </style>
    """

    
    st.markdown(page_bg, unsafe_allow_html=True)


    def translate_text(text, dest_language):
        language_codes = {
            'English': 'en',
            'Hindi': 'hi',
            'Gujarati': 'gu',
            'Marathi': 'mr'
        }
        return translator.translate(text, dest=language_codes[dest_language]).text

    def translate_page(elements, target_language):
        translated_elements = [translate_text(element, target_language) for element in elements]
        return translated_elements

   
    def load_image(image_file):
        img = open(image_file, 'rb').read()
        return img

    
    @st.cache_data  
    def load_data():
        df = pd.read_excel('water.xlsx')  

    df = load_data()

   
    if 'mode' not in st.session_state:
        st.session_state['mode'] = None

    
    language = st.sidebar.selectbox(
        'Select Language',
        ('English', 'Hindi', 'Gujarati', 'Marathi'),
        key="language_selection"
    )

    
    if st.session_state['mode'] == 'search':
        st.write(translate_text("Running search page...", language))
        try:
            search_module = importlib.import_module("search")
            search_module.run()
        except AttributeError:
            st.error("The `search.py` does not have a `run()` function.")
        return

    elif st.session_state['mode'] == 'scan':
        st.write(translate_text("Running scan page...", language))
        try:
            scan_module = importlib.import_module("scan")
            scan_module.run()
        except AttributeError:
            st.error("The `scan.py` does not have a `run()` function.")
        return

    
    st.header(translate_text("Water Footprint Calculator", language))

   
    col1, col2 = st.columns(2)  

    with col1:
        
        st.image("face-scan.png", caption=translate_text("Click for more information", language), use_column_width=True)  # Replace 'image1.jpg' with your actual image
        if st.button(translate_text("Go to Link 1 (Scan)", language)):
            st.session_state['mode'] = 'scan'  
            st.experimental_rerun() 

    with col2:
        
        st.image("magnifying-glass.png", caption=translate_text("Click for more information", language), use_column_width=True)  # Replace 'image2.jpg' with your actual image
        if st.button(translate_text("Go to Link 2 (Search)", language)):
            st.session_state['mode'] = 'search'  
            st.experimental_rerun()  
