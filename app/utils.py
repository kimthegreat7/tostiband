import pandas as pd
import streamlit as st
import base64

@st.cache(suppress_st_warning=True)
def read_data(path):
    return pd.read_csv(path)

@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Tostiband Karaoke-bangers
        </h1>
    """, unsafe_allow_html=True
                )

    st.caption("""
        <p style='text-align: center'>
        by <a href='https://medium.com/geoclid'>Geoclid</a>
        </p>
    """, unsafe_allow_html=True
               )

    st.write(
        "Weet je al wat je gaat zingen?",
        "Een liedje dat nog niet eerder is gezongen?",
        "Selecteer je liedje uit de lijst en voeg hem toe aan de playlist \U0001F642."
    )

def body(sample):
    # name = sample.iloc[0, 0]
    # link = sample.iloc[0, 1]
    # prob = sample.iloc[0, 2]
    st.info(f'### {sample}')
    st.write(sample)
    st.caption(f'[source]({sample})')
    st.markdown('---')
