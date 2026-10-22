import streamlit as st
from database import list_of_cards,list_of_cards_indeks

def cards():
    df=list_of_cards()
    df["kopiuj"] = ":material/open_in_new: Kopiuj"
    st.dataframe(df,column_config={
        "kopiuj": st.column_config.ButtonColumn(
            "kopiuj", type="secondary", on_click=handle_click,key="copy_click",args=(df,)
        )
    })
