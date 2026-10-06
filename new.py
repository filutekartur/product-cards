import streamlit as st

def new():
    st.title("Nowa karta",text_alignment="center")
    with st.form(key="karta"):
        st.number_input("indeks",key="index",step=1)
        st.text_input("pkwiu",key="pkwiu")
        st.datetime_input("data_aktualizacji",key="date_upd",format="YYYY-MM-DD")
        st.datetime_input("data_wprowadzenia",key="date_ins",format="YYYY-MM-DD")
        st.text_input("tworca",key="owner")
        st.text_input("aktualizujacy",key="updater")
        st.text_input("cechy",key="characteristic")
        st.text_input("konsystencja",key="consistency")
        st.text_input("barwa",key="color")
        st.text_input("zapach",key="smell")
        st.text_input("forma_pakowania",key="package")
        st.text_input("etykieta",key="label")
        #st.file_uploader("zdjecia",key="image",type="image/*")
        st.form_submit_button()