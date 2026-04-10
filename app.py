import streamlit as st

st.title("🧠 Simulateur kiné AVC interactif (V1)")

st.write("Modélisation fonctionnelle d'un patient AVC et effets des interventions kinésithérapiques.")

# ----------------------------
# 1. INITIALISATION PATIENT
# ----------------------------

if "patient" not in st.session_state:

    st.session_state.patient = {
        "motricite_MS": 40,   # membre supérieur
        "motricite_MI": 45,   # membre inférieur
        "equilibre": 40,
        "spasticite": 60,
        "controle_moteur": 35
    }

patient = st.session_state.patient

# ----------------------------
# 2. AFFICHAGE ETAT ACTUEL
# ----------------------------

st.subheader("👤 État fonctionnel du patient (0 = mauvais / 100 = normal)")

st.write("**Motricité membre supérieur :**", patient["motricite_MS"])
st.write("**Motricité membre inférieur :**", patient["motricite_MI"])
st.write("**Équilibre :**", patient["equilibre"])
st.write("**Contrôle moteur :**", patient["controle_moteur"])
st.write("**Spasticité (inverse fonctionnel) :**", patient["spasticite"])

# ----------------------------
# 3. TRADUCTION CLINIQUE
# ----------------------------

st.subheader("🧠 Lecture clinique")

if patient["motricite_MI"] < 50:
    st.write("➡️ Hémiparésie des membres inférieurs")
    st.write("➡️ Risque de circumduction / instabilité à la marche")

if patient["spasticite"] > 50:
    st.write("➡️ Spasticité modérée à importante")
    st.write("➡️ Risque de pied équin et raideur")

if patient["equilibre"] < 50:
    st.write("➡️ Trouble de l'équilibre")
    st.write("➡️ Risque de chute augmenté")

# ----------------------------
# 4. INTERVENTIONS KINE
# ----------------------------

st.subheader("🎮 Interventions kinésithérapiques")

col1, col2, col3 = st.columns(3)

# --- Equilibre ---
with col1:
    if st.button("Travail équilibre"):
        patient["equilibre"] += 10
        patient["controle_moteur"] += 5
        patient["spasticite"] -= 5
        st.success("✔ Amélioration de l'équilibre")

# --- Renforcement ---
with col2:
    if st.button("Renforcement moteur"):
        patient["motricite_MS"] += 8
        patient["motricite_MI"] += 8
        patient["controle_moteur"] += 5
        st.success("✔ Amélioration motricité")

# --- Inhibition spasticité ---
with col3:
    if st.button("Inhibition spasticité"):
        patient["spasticite"] -= 15
        patient["controle_moteur"] += 5
        st.success("✔ Diminution spasticité")

# ----------------------------
# 5. LIMITES DES VALEURS
# ----------------------------

for key in patient:
    if patient[key] > 100:
        patient[key] = 100
    if patient[key] < 0:
        patient[key] = 0

# ----------------------------
# 6. RESET PATIENT
# ----------------------------

st.subheader("🔄 Réinitialisation")

if st.button("Reset patient"):
    st.session_state.patient = {
        "motricite_MS": 40,
        "motricite_MI": 45,
        "equilibre": 40,
        "spasticite": 60,
        "controle_moteur": 35
    }
    st.success("Patient réinitialisé")
