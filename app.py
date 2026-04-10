import streamlit as st

st.title("🧠 Simulateur kiné AVC interactif (V6)")

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
# MODE
# ----------------------------

mode = st.selectbox(
    "Mode d’apprentissage",
    ["🦶 Marche", "📈 Évolution", "🎓 ECOS kiné", "🤖 Tuteur IA"]
)

# =========================================================
# 🦶 1. MARCHE (VISUEL KINE)
# =========================================================

if mode == "🦶 Marche":

    st.subheader("🚶 Analyse de la marche")

    marche = (p["controle_selectif"] + p["equilibre"]) / 2

    st.write("Score marche :", int(marche))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Phase d'appui")
        if marche > 70:
            st.write("🟢 stable")
        elif marche > 50:
            st.write("🟠 instable")
        else:
            st.write("🔴 très instable")

    with col2:
        st.write("Phase oscillante")
        if p["controle_selectif"] > 50:
            st.write("🟢 contrôle correct")
        else:
            st.write("🔴 circumduction / bloc")

    with col3:
        st.write("Bras")
        if p["synergie_extension_MI"] > 60:
            st.write("🔴 absence de balancement")
        else:
            st.write("🟢 balancement partiel")

    st.write("🎞️ Simulation visuelle : 🦶—🦶 / 🦶🦶 / 🦶——🦶")

# =========================================================
# 📈 2. EVOLUTION
# =========================================================

elif mode == "📈 Évolution":

    st.subheader("📊 Évolution du patient")

    st.write(f"Jour actuel : J{p['jour']}")

    if st.button("Avancer de 7 jours"):

        p["jour"] += 7

        # progression naturelle rééducation
        p["controle_selectif"] += 2
        p["equilibre"] += 3
        p["spasticite_MI"] -= 2

    st.write("Contrôle moteur :", p["controle_selectif"])
    st.write("Équilibre :", p["equilibre"])
    st.write("Spasticité MI :", p["spasticite_MI"])

    if p["jour"] >= 30:
        st.success("Phase de récupération subaiguë atteinte")

# =========================================================
# 🎓 3. ECOS KINE
# =========================================================

elif mode == "🎓 ECOS kiné":

    st.subheader("🎓 Station clinique ECOS")

    st.write("Patient AVC avec hémiparésie et troubles de la marche.")

    question = st
