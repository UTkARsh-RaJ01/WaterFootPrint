import streamlit as st
import importlib
import base64
from googletrans import Translator

def run():
   
    translator = Translator()

    
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

   
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    
    gif_path = "back.gif"  

    
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

    
    language = st.sidebar.selectbox(
        'Select Language',
        ('English', 'Hindi', 'Gujarati', 'Marathi'),
        key="language_selection_home"  
    )

    
    home_heading = "Preserve Every Drop: Act Now to Conserve Water for a Sustainable Future"
    home_text = "Understanding your water footprint is key to making informed choices that reduce water consumption and promote sustainable living."

    translated_content = translate_page([home_heading, home_text], language)

    
    st.markdown(f'<h1 class="custom-heading">{translated_content[0]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="black-text">{translated_content[1]}</p>', unsafe_allow_html=True)
