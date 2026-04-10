import streamlit as st
import random

st.title("🧠 Simulation patient AVC")

nom = st.text_input("Nom du patient")
age = st.slider("Âge du patient", 40, 100, 70)

if st.button("Créer patient"):

    st.subheader("👤 Patient généré")

    st.write(f"Nom : {nom}")
    st.write(f"Âge : {age} ans")

    st.write("🧠 Simulation en cours...")

    # Déficiences possibles
    deficiences = [
        "Hémiparésie (faiblesse d’un côté du corps)",
        "Aphasie (troubles du langage)",
        "Troubles de l’équilibre",
        "Négligence spatiale",
        "Troubles de la coordination"
    ]

    selection = random.sample(deficiences, 3)

    st.subheader("⚠️ Déficiences probables")

    for d in selection:
        st.write("• " + d)

    st.subheader("🧍 Comportement")

    st.write("Le patient présente une lenteur dans les mouvements et une fatigabilité importante.")
