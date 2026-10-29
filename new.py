import streamlit as st
import json
from database import insert_card,card_by_id
from datetime import datetime
import ast
from navigation import change_view

def new():
    cards_data={}
    st.title("Nowa karta",text_alignment="center")
    indeks_form()
    if st.session_state.indeks:
        with st.container(border=True):
            cards_data.update(form())
    if cards_data:
        dialog_confirmation(cards_data)

def create_from_copy():
    card = card_by_id(st.session_state.card_id)
    card_dict = ast.literal_eval(card["data"].iloc[0])
    template = card_dict.pop("template")
    version = card_dict.pop("version")
    fill_session_keys(card_dict,template)
    new()

def indeks_form():
    with st.container(border=True):
            l,r=st.columns([5,9],wrap=False)
            l.text_input("Indeks",key="indeks")
            if not st.session_state.indeks:
                return
            error = valid_indeks(st.session_state.indeks)
            r.write("")
            r.write("")
            if error:
                r.markdown(f":red[✗] :red[{error}]")
                return
            r.markdown(":green[✓] :green[Indeks OK]")
            if l.button("Pobierz dane z bazy",width="stretch"):
                r.write("")
                r.markdown(":green[✓] :green[Pobrano]")

def form():
    st.selectbox("Szablon",["","podroby_1","podroby_2"],placeholder="Wybierz szablon",key="template")
    card_data={"indeks":st.session_state.indeks}
    if st.session_state.template:
        with st.form(key="card"):
            fields=read_file(f"templates/{st.session_state.template}")
            for p in fields:
                if p["key"] == "indeks":
                    continue
                if p["type"]=="text_input":
                    st.text_input(p["label"],key=p["key"])
                if p["type"]=="number_input":
                    st.number_input(p["label"],key=p["key"])
                if p["type"]=="datetime_input":
                    st.date_input(p["label"],key=p["key"],format="YYYY-MM-DD")
                card_data[p["key"]]=st.session_state[p["key"]]
            if st.form_submit_button("Dalej"):
                card_data["template"]=st.session_state["template"]
                card_data["created_at"]=card_data["created_at"].strftime("%Y-%m-%d")
                card_data["updated_at"]=card_data["updated_at"].strftime("%Y-%m-%d")
                return card_data
    return {}

@st.dialog("Podsumowanie karty")
def dialog_confirmation(data):
    st.dataframe(data)
    if st.button("Zatwierdź",key="approve"):
        insert_card(data)
        change_view("home")

def valid_indeks(indeks):
    if len(indeks)!=8:
        return "Indeks musi mieć dokładnie 8 znaków"
    if not indeks.isascii() or not indeks.isdigit():
        return "Indeks może zawierać wyłącznie cyfry 0-9"

def fill_session_keys(card_data,card_template):
    fields=read_file(f"templates/{card_template}")
    for field in fields:
        if field["type"] == "datetime_input":
            None
        else:
            st.session_state[field["key"]]=card_data[field["key"]]
    st.session_state["template"]=card_template

def read_file(file_name):
    with open(f"{file_name}.json", encoding="utf-8") as f:
        content=json.loads(f.read())
    return content
