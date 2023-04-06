import streamlit as st
import qrcode
import requests
import tempfile
import os
import pandas as pd

image_data = [
    {
        "src": os.path.join("static", "images", "book.jpg"),
        "link": "https://recommendmeabook.com/",
        "caption": "Find A New Book"
    },
    {
        "src": os.path.join("static", "images", "bitcoin.png"),
        "link": "https://www.satoshipapers.org/",
        "caption": "The Satoshi Papers"
    },
    {
        "src": os.path.join("static", "images", "coffee.png"),
        "link": "https://en.wikipedia.org/wiki/Coffee",
        "caption": "What is Coffee?"
    }
]

def render_image_tiles(image_data, num_columns=3):
    cols = st.columns(num_columns)

    for idx, image_info in enumerate(image_data):
        col = cols[idx % num_columns]
        with col:
            col.image(image_info['src'], width=200)
            #link='check out this [link](https://retailscope.africa/)'
            col.markdown(f'<a href="{image_info["link"]}">{image_info["caption"]}</a>',unsafe_allow_html=True)

def create_temp_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"Hello, Streamlit!")
    temp_file.close()
    return temp_file.name


def profile_page():
    # Add a column layout with 3 columns: left (empty), center (content), and right (empty)
    col1, col2, col3 = st.columns([1, 1, 1])

    # Add your profile picture
    image_path = os.path.join("static", "images", "pro_pic.jpeg")
    col2.image(image_path, width=200)

    st.header("Hi, I'm Austin.")

    st.text("Here are some articles I wrote...")
    render_image_tiles(image_data)


    


    