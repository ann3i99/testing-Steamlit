import streamlit as st

st.set_page_config(page_title="test", 
                   page_icon=":shark:", 
                   layout="wide")

st.markdown("# Hello World!")
st.sidebar.write("this is main page")
from PIL import Image
im = Image.open('dellLogo.png')
st.image(im, width=300)