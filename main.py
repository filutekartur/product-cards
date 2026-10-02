import streamlit as st

def change_view(page,card_id=None):
    st.session_state.page=page
    st.session_state.card_id=card_id
    st.rerun()
