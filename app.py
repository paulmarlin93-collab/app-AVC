import streamlit as st

st.title("🧠 Simulation patient AVC")

st.write("Bienvenue dans ton application !")

nom = st.text_input("Nom du patient")
age = st.slider("Âge", 0, 100, 65)

if st.button("Créer patient"):
    st.write(f"Patient {nom}, {age} ans")
    st.write("Simulation en cours...")
