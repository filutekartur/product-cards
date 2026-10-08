import streamlit as st

conn = st.connection('prodcard', type='sql')

def list_of_cards():
    cards=conn.query('select * from cards')
    return cards

def list_of_cards_index(index):
    cards=conn.query(f'select * from cards where indeks = {index}')
    return cards

st.dataframe(list_of_cards())
st.dataframe(list_of_cards_index(800000000))