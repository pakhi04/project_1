import streamlit as st
import os

st.title('Fashion Recommender System')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads',uploaded_file.name)) as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0


#Steps
#File upload -> save
uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        #file has been uploaded
        pass
else:
    st.header("Some error ocurred in the file uploaded")
#load file -> feature extract
#recommendation