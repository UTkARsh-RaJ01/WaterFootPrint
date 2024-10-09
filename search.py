import streamlit as st
import pandas as pd
import base64
from googletrans import Translator

def run():
   
    translator = Translator()
    
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    
    gif_path = "back6.gif"  

    
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
        df = pd.read_excel('wateer.xlsx')  
        return df

   
    df = load_data()

    
    ##st.sidebar.title("Navigation")

    language = st.sidebar.selectbox(
        'Select Language',
        ('English', 'Hindi', 'Gujarati', 'Marathi')
    )

   
    sidebar_titles = ["Go to", "Home", "About", "Calculate Water Footprint", "Know Your Daily Footprint"]
    translated_sidebar = translate_page(sidebar_titles, language)

    
    option = st.sidebar.radio(translated_sidebar[0], [translated_sidebar[1], translated_sidebar[2], translated_sidebar[3], translated_sidebar[4]], index=2)

    
    if option == translated_sidebar[1]:  
        st.markdown(f'<h1 style="color: black; margin-left: 20px;">{translate_text("Welcome to the Landing Page", language)}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: black; margin-left: 20px;">{translate_text("Welcome to our homepage where you can learn more about our app and features!", language)}</p>', unsafe_allow_html=True)

    elif option == translated_sidebar[2]: 
        st.header(translate_text("About Us", language))
        st.markdown(f"## {translate_text('About', language)}")
        st.write(translate_text("This application helps you calculate something special. Learn more about our mission and services.", language))

    elif option == translated_sidebar[3]:  
        st.header(translate_text("Water Footprint Calculator", language))

        
        sub_option = st.sidebar.radio(translate_text("Choose an option:", language), [translate_text("Search", language), translate_text("Scan", language)], index=0)

        if sub_option == translate_text("Search", language):
           
            item = st.selectbox(translate_text("Select an item:", language), df['Item'].unique())

            
            quantity = st.number_input(translate_text("Enter quantity (in kg):", language), min_value=0, value=1)

            
            if st.button(translate_text("Calculate Water Footprint", language)):
                
                item_waterfootprint = df[df['Item'] == item]['WaterFootprint'].values[0]  

                
                total_waterfootprint = item_waterfootprint * quantity

               
                st.write(f"{translate_text('The total water footprint for', language)} {quantity} kg {translate_text('of', language)} {item} {translate_text('is', language)} {total_waterfootprint:.2f}, {translate_text('bottles of water', language)}.")

                
                st.image(load_image("wb.jpg"), caption=translate_text("Water Footprint", language), use_column_width=False, width=300)

        elif sub_option == translate_text("Scan", language):
            
            st.write(translate_text("Scan functionality is currently under development. Please check back later.", language))

    elif option == translated_sidebar[4]:  
        st.header(translate_text("Know Your Daily Footprint", language))
        st.write(translate_text("You can enter the data for your daily activities and calculate your daily water footprint.", language))

