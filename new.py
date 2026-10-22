import streamlit as st
import json
from database import insert_card,card_by_id
from datetime import datetime

def form():
    st.selectbox("Szablon",["","podroby_1","podroby_2"],placeholder="Wybierz szablon",key="template")
    keys={"indeks":st.session_state.indeks}
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
                keys[p["key"]]=st.session_state[p["key"]]
            if st.form_submit_button():
                keys["template"]=st.session_state["template"]
                keys["created_at"]=keys["created_at"].strftime("%Y-%m-%d")
                keys["updated_at"]=keys["updated_at"].strftime("%Y-%m-%d")
                return keys
    return {}

def read_file(file_name):
    with open(f"{file_name}.json", encoding="utf-8") as f:
        content=json.loads(f.read())
    return content

def valid_indeks(indeks):
    if len(indeks)!=8:
        return "Indeks musi mieć dokładnie 8 znaków"
    if not indeks.isascii() or not indeks.isdigit():
        return "Indeks może zawierać wyłącznie cyfry 0-9"

def new():
    cards_data={}
    if "lock" not in st.session_state:
        st.session_state.lock = False
    st.title("Nowa karta",text_alignment="center")
    with st.container(border=True):
        l,r=st.columns([5,9])
        l.text_input("Indeks",key="indeks")
        if st.session_state.indeks:
            val = valid_indeks(st.session_state.indeks)
            if not val:
                r.write("")
                r.write("")
                r.markdown(":green[✓]")
                if l.button("Zatwierdz"):
                    st.session_state.lock = True
                    st.rerun()
            else:
                r.write("")
                r.write("")
                r.markdown(f":red[✗] :red[{val}]")
    if st.session_state.indeks and st.session_state.lock:
        r.write("")
        r.markdown(":green[✓]")
        with st.container(border=True):
            cards_data.update(form())
    if cards_data:
        insert_card(cards_data)

def create_from_copy():
    card = card_by_id(st.session_state.card_id)