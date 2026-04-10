import streamlit as st
import random

st.title("🧠 Générateur de cas clinique AVC (IA)")

nom = st.text_input("Nom du patient")
age = st.slider("Âge", 40, 100, 70)

niveau = st.selectbox("Sévérité de l'AVC", ["Léger", "Modéré", "Sévère"])

if st.button("Générer cas clinique"):

    st.subheader("👤 Patient")

    st.write(f"Nom : {nom}")
    st.write(f"Âge : {age}")
    st.write(f"Sévérité : {niveau}")

    st.subheader("🧠 Cas clinique généré")

    # logique simple mais cohérente
    if niveau == "Léger":
        deficits = [
            "Faiblesse légère d’un membre supérieur",
            "Légers troubles du langage",
            "Fatigabilité à l’effort"
        ]
        evolution = "Bonne récupération attendue avec rééducation"

    elif niveau == "Modéré":
        deficits = [
            "Hémiparésie partielle",
            "Aphasie modérée",
            "Troubles de la marche"
        ]
        evolution = "Récupération partielle possible avec séquelles"

    else:
        deficits = [
            "Hémiplégie importante",
            "Aphasie sévère",
            "Perte d’autonomie"
        ]
        evolution = "Pronostic réservé, dépend de la prise en charge"

    st.subheader("⚠️ Déficits")

    for d in deficits:
        st.write("• " + d)

    st.subheader("📈 Évolution probable")
    st.write(evolution)

    st.subheader("🧾 Synthèse IA")
    st.write(
        f"Patient de {age} ans présentant un AVC {niveau.lower()} avec "
        f"atteinte neurologique compatible. Nécessite prise en charge neuro-rééducative."
    )
