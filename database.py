import streamlit as st

conn = st.connection('prodcard', type='sql')

def list_of_cards():
    cards=conn.query('select * from cards')
    return cards

st.dataframe(list_of_cards())