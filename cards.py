import streamlit as st
from database import list_of_cards,list_of_cards_indeks,card_by_id
from navigation import change_view
from new import fill_session_keys
import ast
from wordtpl import dictobin

def handle_click(table):
    click=st.session_state.action_click
    card_id = int(table.loc[click["row"]]["id"])
    if "Kopiuj" in click["label"]:
        change_view("create_from_copy",card_id)
    if "Pobierz" in click["label"]:
        dialog_download(card_id)

def cards():
    df=list_of_cards()
    df["more"] = [[":material/edit_document: Kopiuj",":material/description: Pobierz"]] * len(df)
    st.dataframe(df,column_config={
        "more": st.column_config.ButtonColumn(
            type="secondary", on_click=handle_click, key="action_click",args=(df,)
        )
    })

@st.dialog("Pobierz")
def dialog_download(card_id):
    card = card_by_id(card_id)
    card_dict = ast.literal_eval(card["data"].iloc[0])#creates dictionary from json from data column
    template = card_dict.pop("template")
    version = card_dict.pop("version")
    fill_session_keys(card_dict,template)
    st.title(f"{card_dict["indeks"]}, V: {version}",text_alignment="center")
    l,r=st.columns(2)
    l.download_button(
        "Word",
        data=lambda: word(card_dict,template),
        file_name=f"{card_dict["indeks"]}_{version}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        icon=":material/description:",
    )
    r.download_button("PDF",data="None")

def word(card_dict,template):
    return dictobin(card_dict,template)