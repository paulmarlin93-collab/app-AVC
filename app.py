import streamlit as st

st.title("🧠 Simulateur clinique kiné AVC interactif (V4)")

# ----------------------------
# PATIENT NEUROLOGIQUE
# ----------------------------

if "patient" not in st.session_state:

    st.session_state.patient = {
        "hemisphere": "Gauche",
        "severite": "Modéré",

        # contrôle moteur fin
        "controle_selectif": 40,

        # synergies
        "synergie_flexion_MS": 70,
        "synergie_extension_MI": 65,

        # tonus
        "spasticite_MS": 60,
        "spasticite_MI": 55,

        # fonction
        "equilibre": 45,
        "marche": 40
    }

p = st.session_state.patient

# ----------------------------
# AFFICHAGE PATIENT
# ----------------------------

st.subheader("👤 Profil neurologique")

st.write("Hémisphère atteint :", p["hemisphere"])
st.write("Sévérité AVC :", p["severite"])

# ----------------------------
# LECTURE CLINIQUE AUTOMATIQUE
# ----------------------------

st.subheader("🧠 Raisonnement clinique")

if p["synergie_flexion_MS"] > 60:
    st.write("➡️ Synergie de flexion MS dominante → perte de dissociation épaule/coude/main")

if p["synergie_extension_MI"] > 60:
    st.write("➡️ Extension MI en bloc → circumduction probable en marche")

if p["spasticite_MI"] > 50:
    st.write("➡️ Spasticité MI → risque équin + appui instable")

if p["controle_selectif"] < 50:
    st.write("➡️ Faible contrôle sélectif → mouvements globalisés / synergies")

# ----------------------------
# SIMULATION MARCHE (VISUEL SIMPLE)
# ----------------------------

st.subheader("🚶 Analyse de la marche")

marche = (p["controle_selectif"] + p["equilibre"]) / 2

if marche > 70:
    st.success("Marche fonctionnelle avec légère asymétrie")
elif marche > 50:
    st.warning("Marche avec compensations visibles (circumduction)")
else:
    st.error("Marche pathologique nécessitant aide")

# ----------------------------
# INTERVENTIONS KINE
# ----------------------------

st.subheader("🎮 Rééducation kinésithérapique")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Facilitation motrice"):
        p["controle_selectif"] += 8
        p["synergie_flexion_MS"] -= 5
        st.success("✔ amélioration contrôle moteur")

with col2:
    if st.button("Inhibition spasticité"):
        p["spasticite_MI"] -= 10
        p["spasticite_MS"] -= 5
        st.success("✔ diminution tonus")

with col3:
    if st.button("Travail équilibre"):
        p["equilibre"] += 10
        p["controle_selectif"] += 3
        st.success("✔ amélioration stabilité")

# ----------------------------
# LIMITES
# ----------------------------

for k in p:
    p[k] = max(0, min(100, p[k]))

# ----------------------------
# RESET
# ----------------------------

if st.button("Reset patient"):
    st.session_state.patient = {
        "hemisphere": "Gauche",
        "severite": "Modéré",
        "controle_selectif": 40,
        "synergie_flexion_MS": 70,
        "synergie_extension_MI": 65,
        "spasticite_MS": 60,
        "spasticite_MI": 55,
        "equilibre": 45,
        "marche": 40
    }
    st.success("Patient réinitialisé")
