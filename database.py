import streamlit as st
from sqlalchemy import text

conn = st.connection('prodcard', type='sql')

def list_of_cards():
    cards=conn.query('select * from cards',ttl=0)
    return cards

def list_of_cards_index(index):
    cards=conn.query(
        'select * from cards where indeks = :index',
        params = {'index': index},
        ttl=0
    )
    return cards

def insert_card(data):
    with conn.session as s:
        s.execute(text(
            """
            INSERT INTO cards (indeks,wersja,data_wprowadzenia,data_modyfikacji,dane) 
            VALUES (:ind,:wer,:data_w,:data_m,:dane)
            """),
            params = {
                "ind":data["indeks"],
                "wer":data["wersja"],
                "data_w":data["data_wprowadzenia"],
                "data_m":data["data_modyfikacji"],
                "dane":data["dane"],
            }
        )
        s.commit()

st.dataframe(list_of_cards())
st.dataframe(list_of_cards_index(800000000))