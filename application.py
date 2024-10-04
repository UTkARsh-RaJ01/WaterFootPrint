import streamlit as st
import importlib


pages = {
    "Home": "home_page",
    "About": "about_page",
    "Know Your Daily Footprint": "daily",
    "Water Footprint Calculate": "main_calculate",
    "Search": "search",
    "Scan": "scan"
}


selection = st.sidebar.radio("Go to", list(pages.keys()))

page_module = importlib.import_module(pages[selection])


page_module.run()

