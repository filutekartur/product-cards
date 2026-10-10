import streamlit as st

def new():
    st.title("Nowa karta",text_alignment="center")
    with st.form(key="card"):
        st.number_input("indeks",key="indeks",step=1)
        st.text_input("pkwiu",key="pkwiu")
        st.datetime_input("data_wprowadzenia",key="created_at",format="YYYY-MM-DD")
        st.datetime_input("data_aktualizacji",key="updated_at",format="YYYY-MM-DD")
        st.text_input("twórca",key="created_by")
        st.text_input("aktualizujacy",key="updated_by")
        st.text_input("cechy",key="characteristic")
        st.text_input("konsystencja",key="consistency")
        st.text_input("barwa",key="color")
        st.text_input("zapach",key="smell")
        st.text_input("forma_pakowania",key="package")
        st.text_input("etykieta",key="label")
        #st.file_uploader("zdjecia",key="image",type="image/*")
        st.form_submit_button()