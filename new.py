import streamlit as st
import json

def form():
    st.selectbox("Szablon",["","podroby_1","podroby_2"],placeholder="Wybierz szablon",key="template")
    if st.session_state.template:
        with st.form(key="card"):
            fields=read_file(f"templates/{st.session_state.template}")
            for p in fields:
                if p["type"]=="text_input":
                    st.text_input(p["label"],key=p["key"])
                if p["type"]=="number_input":
                    st.number_input(p["label"],key=p["key"])
                if p["type"]=="datetime_input":
                    st.date_input(p["label"],key=p["key"],format="YYYY-MM-DD")
            st.form_submit_button()

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
    st.title("Nowa karta",text_alignment="center")
    with st.form(key="card"):
        st.number_input("Indeks",key="indeks",step=1)
        st.text_input("Pkwiu",key="pkwiu")
        st.datetime_input("Data_wprowadzenia",key="created_at",format="YYYY-MM-DD")
        st.datetime_input("Data_aktualizacji",key="updated_at",format="YYYY-MM-DD")
        st.text_input("Twórca",key="created_by")
        st.text_input("Aktualizujacy",key="updated_by")
        st.text_input("Cechy",key="characteristic")
        st.text_input("Konsystencja",key="consistency")
        st.text_input("Barwa",key="color")
        st.text_input("Zapach",key="smell")
        st.text_input("Forma_pakowania",key="package")
        st.text_input("Etykieta",key="label")
        #st.file_uploader("zdjecia",key="image",type="image/*")
        st.form_submit_button()