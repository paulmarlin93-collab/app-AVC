import streamlit as st

st.title("🧠 Simulateur clinique kiné AVC interactif (V4)")

# ----------------------------
# PATIENT NEUROLOGIQUE
# ----------------------------

if "patient" not in st.session_state:

    st.session_state.patient = {
        # variables qualitatives (NON numériques)
        "hemisphere": "Gauche",
        "severite": "Modéré",

        # variables numériques
        "controle_selectif": 40,
        "synergie_flexion_MS": 70,
        "synergie_extension_MI": 65,
        "spasticite_MS": 60,
        "spasticite_MI": 55,
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
# RAISONNEMENT CLINIQUE
# ----------------------------

st.subheader("🧠 Raisonnement clinique")

if p["synergie_flexion_MS"] > 60:
    st.write("➡️ Synergie de flexion MS dominante → perte de dissociation MS")

if p["synergie_extension_MI"] > 60:
    st.write("➡️ Synergie extension MI → circumduction probable en marche")

if p["spasticite_MI"] > 50:
    st.write("➡️ Spasticité MI → risque équin + instabilité")

if p["controle_selectif"] < 50:
    st.write("➡️ Faible contrôle sélectif → mouvements globalisés")

# ----------------------------
# MARCHE
# ----------------------------

st.subheader("🚶 Analyse de la marche")

marche = (p["controle_selectif"] + p["equilibre"]) / 2

st.write("Score marche :", int(marche))

if marche > 70:
    st.success("Marche fonctionnelle avec légère asymétrie")
elif marche > 50:
    st.warning("Marche avec compensations (circumduction possible)")
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
        st.success("✔ contrôle moteur amélioré")

with col2:
    if st.button("Inhibition spasticité"):
        p["spasticite_MI"] -= 10
        p["spasticite_MS"] -= 5
        st.success("✔ tonus diminué")

with col3:
    if st.button("Travail équilibre"):
        p["equilibre"] += 10
        p["controle_selectif"] += 3
        st.success("✔ stabilité améliorée")

# ----------------------------
# LIMITES (CORRIGÉ)
# ----------------------------

numeric_keys = [
    "controle_selectif",
    "synergie_flexion_MS",
    "synergie_extension_MI",
    "spasticite_MS",
    "spasticite_MI",
    "equilibre",
    "marche"
]

for k in numeric_keys:
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
