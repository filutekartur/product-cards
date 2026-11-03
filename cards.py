import streamlit as st
from database import list_of_cards,list_of_cards_indeks
from navigation import change_view

def handle_click(table):
    click=st.session_state.action_click
    card_id = int(table.loc[click["row"]]["id"])
    if "Kopiuj" in click["label"]:
        change_view("create_from_copy",card_id)
    if "Pobierz" in click["label"]:
        None

def cards():
    df=list_of_cards()
    df["more"] = [[":material/edit_document: Kopiuj",":material/description: Pobierz"]] * len(df)
    st.dataframe(df,column_config={
        "more": st.column_config.ButtonColumn(
            type="secondary", on_click=handle_click, key="action_click",args=(df,)
        )
    })
