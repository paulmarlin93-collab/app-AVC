import streamlit as st
import matplotlib.pyplot as plt

st.title("🧠 Simulateur kiné AVC interactif (V2)")

st.write("Visualisation fonctionnelle + simulation de marche + effets des interventions.")

# ----------------------------
# ETAT PATIENT
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
# BARRES VISUELLES
# ----------------------------

st.subheader("📊 Profil fonctionnel du patient")

labels = list(p.keys())
values = list(p.values())

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylim(0, 100)
ax.set_ylabel("Score fonctionnel")
ax.set_title("Profil moteur du patient AVC")

st.pyplot(fig)

# ----------------------------
# LECTURE CLINIQUE
# ----------------------------

st.subheader("🧠 Lecture clinique")

if p["motricite_MI"] < 50:
    st.write("➡️ Hémiparésie MI → instabilité à la marche")

if p["spasticite"] > 50:
    st.write("➡️ Spasticité élevée → risque pied équin")

if p["equilibre"] < 50:
    st.write("➡️ Trouble équilibre → risque de chute")

# ----------------------------
# SIMULATION DE MARCHE
# ----------------------------

st.subheader("🚶 Simulation de marche (fonctionnelle)")

# score global marche
marche = (p["motricite_MI"] + p["equilibre"] + p["controle_moteur"]) / 3

st.write(f"Score global de marche : {int(marche)}/100")

if marche > 70:
    st.success("🚶 Marche quasi normale avec légère asymétrie")
elif marche > 50:
    st.warning("🚶 Marche instable avec compensation visible (circumduction possible)")
elif marche > 30:
    st.error("🚶 Marche difficile avec aide nécessaire")
else:
    st.error("🚶 Déambulation impossible sans assistance")

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
        st.success("Amélioration équilibre")

with col2:
    if st.button("Renforcement"):
        p["motricite_MS"] += 8
        p["motricite_MI"] += 8
        p["controle_moteur"] += 5
        st.success("Amélioration motricité")

with col3:
    if st.button("Inhibition spasticité"):
        p["spasticite"] -= 15
        p["controle_moteur"] += 5
        st.success("Spasticité réduite")

# ----------------------------
# LIMITES
# ----------------------------

for k in p:
    p[k] = max(0, min(100, p[k]))

# ----------------------------
# RESET
# ----------------------------

st.subheader("🔄 Reset")

if st.button("Réinitialiser patient"):
    st.session_state.patient = {
        "motricite_MS": 40,
        "motricite_MI": 45,
        "equilibre": 40,
        "spasticite": 60,
        "controle_moteur": 35
    }
    st.success("Patient réinitialisé")
