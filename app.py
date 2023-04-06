import streamlit as st
import os
from profile_page import profile_page
from home import home
from tip import tip
# Import other pages here, e.g.
# from other_page_1 import other_page_1
# from other_page_2 import other_page_2

# Set the app title
st.set_page_config(page_title="My Streamlit App", page_icon=None, layout='wide')

# Create a sidebar menu for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard ₿", "About Me 😎", "Send a Lightning Tip ⚡"])

# Render the selected page
if page == "Dashboard ₿":
    home()
elif page == "About Me 😎":
    profile_page()
elif page == "Send a Lightning Tip ⚡":
    tip()
# elif page == "Other Page 2":
#     other_page_2()