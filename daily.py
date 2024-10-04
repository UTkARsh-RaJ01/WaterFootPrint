import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from googletrans import Translator

def run():
    st.title("Know Your Daily Footprint")

    
    translator = Translator()

    
    def translate_text(text, dest_language):
        language_codes = {
            'English': 'en',
            'Hindi': 'hi',
            'Gujarati': 'gu',
            'Marathi': 'mr'
        }
        return translator.translate(text, dest=language_codes[dest_language]).text

   
    @st.cache_data
    def load_data():
        df = pd.read_excel('water.xlsx')  
        return df

    
    df = load_data()

    
    if 'basket' not in st.session_state:
        st.session_state['basket'] = [] 

   
    with st.form(key='add_to_basket_form'):
        item = st.selectbox("Select an item:", df['Item'].unique())
        quantity = st.number_input("Enter quantity (in kg):", min_value=0, value=1)
        add_button = st.form_submit_button(label="Add to Basket")

        
        if add_button:
            item_waterfootprint = df[df['Item'] == item]['WaterFootprint'].values[0]
            st.session_state['basket'].append({'item': item, 'quantity': quantity, 'waterfootprint': item_waterfootprint * quantity})
            st.success(f"{quantity} kg of {item} added to the basket!")

    
    if st.session_state['basket']:
        st.write("### Basket Contents")
        basket_df = pd.DataFrame(st.session_state['basket'])
        st.write(basket_df)

        
        if st.button("Calculate Total Water Footprint"):
            total_footprints = basket_df.groupby('item').sum()['waterfootprint']
            fig, ax = plt.subplots()
            ax.pie(total_footprints, labels=total_footprints.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
    else:
        st.write("Your basket is empty. Please add items to see the water footprint calculation.")
