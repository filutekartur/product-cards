import streamlit as st
from new import new

def change_view(page,card_id=None):
    st.session_state.page=page
    st.session_state.card_id=card_id
    st.rerun()

def home():
    st.title("Karty produktów",text_alignment="center")
    l_col,m_col,r_col  = st.columns(3,border=True)
    with l_col:
        st.write("Twórz nową kartę")
        if st.button("new"):
            change_view("new")
    with m_col:
        st.write("Przeglądaj karty")
        if st.button("clist"):
            change_view("clist")
    with r_col:
        st.write("Przeglądaj słowniki")
        if st.button("dictionary"):
            change_view("dictionary")


pages = {
    "home" : home,
    "new" : new
}

if "page" not in st.session_state:
    st.session_state.page = "home"
if not st.session_state.page=="home":
    st.button("home",on_click=change_view,args=("home",))

pages[st.session_state.page]()
