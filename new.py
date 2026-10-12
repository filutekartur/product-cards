import streamlit as st

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