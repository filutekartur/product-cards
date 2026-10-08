import streamlit as st

conn = st.connection('prodcard', type='sql')

def list_of_cards():
    cards=conn.query('select * from cards')
    return cards

def list_of_cards_index(index):
    cards=conn.query(
        'select * from cards where indeks = :index',
        params = {'index': index}
        )
    return cards

def insert_card(data):
    with conn.session as s:
        s.execute()
        s.commit()
    return 1

st.dataframe(list_of_cards())
st.dataframe(list_of_cards_index(800000000))