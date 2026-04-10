import streamlit as st
import random

st.title("🧠 Simulateur kiné AVC interactif (V5 - Formation avancée)")

# ----------------------------
# PATIENT
# ----------------------------

if "patient" not in st.session_state:
    st.session_state.patient = {
        "controle_selectif": 40,
        "synergie_flexion_MS": 70,
        "synergie_extension_MI": 65,
        "spasticite_MS": 60,
        "spasticite_MI": 55,
        "equilibre": 45,
        "marche": 40,
        "jour": 0
    }

p = st.session_state.patient

# ----------------------------
# NAVIGATION SIMPLE
# ----------------------------

mode = st.selectbox(
    "Mode d’apprentissage",
    ["🦶 Marche", "📈 Évolution", "🧠 Cas clinique", "🤖 Tuteur IA"]
)

# =========================================================
# 🦶 1. ANIMATION DE MARCHE (SIMPLE VISUEL KINE)
# =========================================================

if mode == "🦶 Marche":

    st.subheader("🚶 Simulation de marche")

    marche = (p["controle_selectif"] + p["equilibre"]) / 2

    if marche > 70:
        st.success("🟢 Marche quasi normale")
        st.write("→ Bon contrôle du membre inférieur")
        st.write("→ Ballant des bras présent")
    elif marche > 50:
        st.warning("🟠 Marche avec compensations")
        st.write("→ Circumduction possible")
        st.write("→ Diminution du ballant du bras")
    else:
        st.error("🔴 Marche pathologique")
        st.write("→ Aide nécessaire")
        st.write("→ Instabilité importante")

    # mini “animation symbolique”
    steps = ["🦶——🦶", "🦶—🦶", "🦶🦶"]
    st.write("Simulation visuelle :", random.choice(steps))

# =========================================================
# 📈 2. EVOLUTION DANS LE TEMPS
# =========================================================

elif mode == "📈 Évolution":

    st.subheader("📊 Évolution du patient")

    st.write(f"Jour actuel : J{p['jour']}")

    if st.button("Avancer dans le temps (+7 jours)"):

        p["jour"] += 7

        # évolution légère naturelle
        p["controle_selectif"] += 2
        p["equilibre"] += 3
        p["spasticite_MI"] -= 2

    st.write("État fonctionnel :")
    st.write("Contrôle moteur :", p["controle_selectif"])
    st.write("Équilibre :", p["equilibre"])
    st.write("Spasticité MI :", p["spasticite_MI"])

    if p["jour"] >= 30:
        st.success("Phase de récupération subaiguë atteinte")

# =========================================================
# 🧠 3. CAS CLINIQUE (TYPE EXAMEN)
# =========================================================

elif mode == "🧠 Cas clinique":

    st.subheader("📋 Cas clinique étudiant")

    cas = random.choice([
        "Patient de 72 ans présentant une hémiparésie droite brutale.",
        "Patient de 65 ans avec troubles de la marche post-AVC ischémique.",
        "Patient avec spasticité importante et perte de sélectivité motrice."
    ])

    st.write(cas)

    question = st.selectbox(
        "Quelle est la priorité kinésithérapique ?",
        [
            "Renforcement musculaire global",
            "Rééducation du contrôle moteur sélectif",
            "Immobilisation prolongée",
            "Travail uniquement passif"
        ]
    )

    if st.button("Valider réponse"):

        if question == "Rééducation du contrôle moteur sélectif":
            st.success("✔ Bonne réponse kinésithérapique")
        else:
            st.error("❌ Réponse non optimale")

# =========================================================
# 🤖 4. TUTEUR IA (EXPLICATION CLINIQUE)
# =========================================================

elif mode == "🤖 Tuteur IA":

    st.subheader("🧠 Analyse kinésithérapique guidée")

    if p["synergie_extension_MI"] > 60:
        st.write("➡️ Synergie extension MI → marche en bloc + circumduction")

    if p["spasticite_MI"] > 50:
        st.write("➡️ Spasticité triceps sural → risque pied équin")

    if p["controle_selectif"] < 50:
        st.write("➡️ Déficit de sélectivité → perte de dissociation segmentaire")

    if p["equilibre"] < 50:
        st.write("➡️ Instabilité posturale → stratégie de compensation")

    st.write("---")
    st.write("💡 Objectif kiné : restaurer le contrôle moteur avant la force brute")
