"""Main program for the streamlit app"""

import streamlit as st
from utils import read_data, head, body, set_bg

st.set_page_config(
    page_title='Tostiband Karaoke bangers',
    page_icon='assets/icon.png'
)

set_bg('assets/fotoband.png')
head()

df_liedjes = read_data('data/karaoke_bangers.csv')
lst_liedjes = [x +' - '+ y for x,y in zip(df_liedjes['Artiest'], df_liedjes['Nummer'])]
song = st.selectbox('Liedjes', lst_liedjes)

if st.button('Bring it on!'):

    # if button is clicked, add song to playlist, remove song from original list

    df = read_data('data/olympiad-problems.csv')
    choice = df.sample(1)
    body(song)

