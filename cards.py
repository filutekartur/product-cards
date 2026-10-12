import streamlit as st
from database import list_of_cards,list_of_cards_indeks

def cards():
    df=list_of_cards()
    st.write(df)