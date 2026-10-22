import streamlit as st
from new import new
from cards import cards
from navigation import change_view

def home():
    st.title("Karty produktów",text_alignment="center")
    l_col,m_col,r_col  = st.columns(3,border=True)
    with l_col:
        st.write("Twórz nową kartę")
        if st.button("new"):
            change_view("new")
    with m_col:
        st.write("Przeglądaj karty")
        if st.button("cards"):
            change_view("cards")
    with r_col:
        st.write("Przeglądaj słowniki")
        if st.button("dictionary"):
            change_view("dictionary")


pages = {
    "home" : home,
    "new" : new,
    "cards" : cards,
}

if "page" not in st.session_state:
    st.session_state.page = "home"
if st.session_state.page != "home":
    st.button("home",on_click=change_view,args=("home",))

pages[st.session_state.page]()
