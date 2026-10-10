import streamlit as st
from sqlalchemy import text

conn = st.connection('prodcard', type='sql')

def list_of_cards():
    cards=conn.query('select * from cards',ttl=0)
    return cards

def list_of_cards_indeks(indeks):
    cards=conn.query(
        'select * from cards where indeks = :indeks',
        params = {'indeks': indeks},
        ttl=0
    )
    return cards

def insert_card(form_data):
    cards = list_of_cards_indeks(form_data["indeks"])
    if cards.shape[0]>0:
        form_data["version"]=int(cards['version'].max())+1
    else:
        form_data["version"]=1
    with conn.session as s:
        s.execute(text(
            """
            INSERT INTO cards (indeks,version,created_at,updated_at,template,data) 
            VALUES (:indeks,:version,:created_at,:updated_at,:template,:data)
            """),
            params = {
                "indeks":form_data["indeks"],
                "version":form_data["version"],
                "created_at":form_data["created_at"],
                "updated_at":form_data["updated_at"],
                "template":form_data["template"],
                "data":str(form_data),
            }
        )
        s.commit()
