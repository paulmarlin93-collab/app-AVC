import streamlit as st
import matplotlib.pyplot as plt

st.title("🧠 Simulateur kiné AVC interactif (V3)")

# ----------------------------
# PATIENT
# ----------------------------

if "patient" not in st.session_state:
    st.session_state.patient = {
        "motricite_MS": 40,
        "motricite_MI": 45,
        "equilibre": 40,
        "spasticite": 60,
        "controle_moteur": 35
    }

p = st.session_state.patient

# ----------------------------
# DASHBOARD GLOBAL
# ----------------------------

st.subheader("📊 Profil fonctionnel")

fig, ax = plt.subplots()
ax.bar(p.keys(), p.values())
ax.set_ylim(0, 100)
st.pyplot(fig)

# ----------------------------
# SCORE GLOBAL KINE
# ----------------------------

st.subheader("🧠 Score clinique global")

autonomie = (p["motricite_MI"] + p["equilibre"] + p["controle_moteur"]) / 3

st.write(f"Autonomie fonctionnelle : {int(autonomie)}/100")

if autonomie > 70:
    st.success("Patient autonome avec légère gêne")
elif autonomie > 50:
    st.warning("Patient partiellement dépendant")
else:
    st.error("Patient dépendant nécessitant aide")

# ----------------------------
# MARCHE (SIMPLIFIEE VISUELLE)
# ----------------------------

st.subheader("🚶 Simulation de marche")

marche = autonomie

if marche > 70:
    st.write("🚶 ➡️➡️ Marche quasi normale")
    st.write("Bras : balancement normal")
elif marche > 50:
    st.write("🚶 ➡️   Marche avec compensation")
    st.write("Bras : diminution du ballant")
else:
    st.write("🚶 ❌ Marche instable / assistance nécessaire")
    st.write("Bras : absence de balancement")

# ----------------------------
# IA EXPLICATIVE (LOGIQUE CLINIQUE)
# ----------------------------

st.subheader("🧠 Analyse kinésithérapique (IA pédagogique)")

if p["motricite_MI"] < 50:
    st.write("➡️ Faiblesse MI → compensation par circumduction lors de la marche")

if p["spasticite"] > 50:
    st.write("➡️ Spasticité élevée → risque de pied équin (triceps sural dominant)")

if p["equilibre"] < 50:
    st.write("➡️ Déficit d'équilibre → stratégie d'élargissement du polygone de sustentation")

if p["controle_moteur"] < 50:
    st.write("➡️ Contrôle moteur réduit → mouvements désorganisés et synergies pathologiques")

# ----------------------------
# INTERVENTIONS KINE
# ----------------------------

st.subheader("🎮 Interventions kinésithérapiques")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Équilibre"):
        p["equilibre"] += 10
        p["controle_moteur"] += 5
        p["spasticite"] -= 5

with col2:
    if st.button("Renforcement"):
        p["motricite_MS"] += 8
        p["motricite_MI"] += 8
        p["controle_moteur"] += 5

with col3:
    if st.button("Inhibition spasticité"):
        p["spasticite"] -= 15
        p["controle_moteur"] += 5

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
        "motricite_MS": 40,
        "motricite_MI": 45,
        "equilibre": 40,
        "spasticite": 60,
        "controle_moteur": 35
    }
    st.success("Patient réinitialisé")
