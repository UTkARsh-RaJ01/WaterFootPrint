import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
from PIL import Image
import tensorflow as tf
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

    
    @st.cache_data
    def load_data():
        df = pd.read_excel('wateer.xlsx')  
        return df

    
    df = load_data()

    
    class_names_model1_model3 = df['Item'].tolist()

   
    class_names_model2 = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot',
                        'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger',
                        'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika',
                        'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach',
                        'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']

    
    @st.cache_resource
    def load_models():
        model1 = load_model('model1.h5')  
        model2 = load_model('FV_1.h5') 
        model3 = load_model('model3.h5')

        return model1, model2, model3

    model1, model2, model3 = load_models()

  
    input_size_model1 = (224, 224)  
    input_size_model2 = (224, 224) 
    input_size_model3 = (150, 150)  

    
    def preprocess_image(image, target_size):
        img = image.resize(target_size)  
        img = np.array(img)
        img = img / 255.0  
        img = np.expand_dims(img, axis=0)  
        return img

    
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

   
    gif_path = "green.gif"  
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
        ('English', 'Hindi', 'Gujarati', 'Marathi')
    )

   
    st.title(translate_text("Water Footprint Estimation from Image", language))

    
    uploaded_file = st.file_uploader(translate_text("Upload an image", language), type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        
        image = Image.open(uploaded_file)
        st.image(image, caption=translate_text("Uploaded Image", language), use_column_width=True)

       
        processed_image1 = preprocess_image(image, input_size_model1)
        processed_image2 = preprocess_image(image, input_size_model2)
        processed_image3 = preprocess_image(image, input_size_model3)

        
        pred1 = model1.predict(processed_image1)
        pred2 = model2.predict(processed_image2)
        pred3 = model3.predict(processed_image3)

        
        identified_item = None
        model_used = None

        
        if np.max(pred2) > 0.5:
            identified_item = class_names_model2[np.argmax(pred2)]
            model_used = "Model 2"
        elif np.max(pred1) > 0.5:
            identified_item = class_names_model1_model3[np.argmax(pred1)]
            model_used = "Model 1"
        elif np.max(pred3) > 0.5:
            identified_item = class_names_model1_model3[np.argmax(pred3)]
            model_used = "Model 3"

        
        if identified_item:
            st.success(f"{translate_text('Identified Item', language)}: {identified_item} ({translate_text('Identified by', language)} {model_used})")

            
            identified_item_cleaned = identified_item.strip().lower()

            
            df['Item_cleaned'] = df['Item'].str.strip().str.lower()
            if identified_item_cleaned in df['Item_cleaned'].values:
                
                water_footprint = df[df['Item_cleaned'] == identified_item_cleaned]['WaterFootprint'].values[0]

               
                quantity = st.number_input(f"{translate_text('Enter quantity of', language)} {identified_item} ({translate_text('in kg', language)}):", min_value=0.0, value=1.0)

                
                if st.button(translate_text("Calculate Water Footprint", language)):
                    
                    image_file_path = 'wb.jpg'
                    st.image(image_file_path, caption=translate_text("Water Footprint", language), use_column_width=False, width=300)

                    
                    total_water_footprint = water_footprint * quantity
                    st.write(f"The total water footprint for {quantity} kg of {identified_item} is {total_water_footprint:.2f} 1-liter bottles.")
            else:
                st.error(f"Item '{identified_item}' not found in the Excel sheet.")
        else:
            st.error("No model was able to identify the image. Please try a different image.")
    else:
        st.write("Please upload an image to begin.")
