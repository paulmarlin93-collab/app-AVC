import streamlit as st

# =========================================================
# 🧠 PATIENT (MODULE)
# =========================================================

def create_patient():
    return {
        "controle": 40,
        "synergie": 70,
        "spasticite": 60,
        "equilibre": 45,
        "jour": 0
    }

# =========================================================
# 🚶 MARCHE (MODULE)
# =========================================================

def marche_score(p):
    return (p["controle"] + p["equilibre"]) / 2


def analyse_marche(p):
    res = []

    if p["synergie"] > 60:
        res.append("Compensation : circumduction probable")

    if p["controle"] < 50:
        res.append("Déficit contrôle moteur sélectif")

    return res

# =========================================================
# 📈 EVOLUTION (MODULE)
# =========================================================

def evolution_patient(p):
    p["jour"] += 7
    p["controle"] += 2
    p["equilibre"] += 3
    p["spasticite"] -= 2
    return p

# =========================================================
# 🎓 ECOS (MODULE)
# =========================================================

def correction_ecos(rep):
    if rep == "Contrôle moteur":
        return True, "✔ Bonne réponse kinésithérapique"
    return False, "❌ Réponse incomplète"

# =========================================================
# 🤖 TUTEUR IA (MODULE)
# =========================================================

def analyse_clinique(p):
    out = []

    out.append("📌 AVC avec hémiparésie")

    if p["synergie"] > 60:
        out.append("➡️ Synergies pathologiques présentes")

    if p["controle"] < 50:
        out.append("➡️ Déficit de contrôle moteur sélectif")

    if p["spasticite"] > 50:
        out.append("➡️ Hypertonie spastique")

    out.append("🎯 Objectif : contrôle moteur avant renforcement")

    return out

# =========================================================
# 🖥️ INTERFACE STREAMLIT
# =========================================================

st.title("🧠 Logiciel kiné AVC - Version V8")

# INIT PATIENT
if "p" not in st.session_state:
    st.session_state.p = create_patient()

p = st.session_state.p

# MENU
mode = st.selectbox(
    "Module clinique",
    ["🦶 Marche", "📈 Évolution", "🎓 ECOS", "🤖 Tuteur"]
)

# =========================================================
# 🦶 MARCHE
# =========================================================

if mode == "🦶 Marche":

    st.subheader("🚶 Analyse de la marche")

    score = marche_score(p)
    st.write("Score marche :", int(score))

    if score > 70:
        st.success("Marche quasi normale")
    elif score > 50:
        st.warning("Marche avec compensations")
    else:
        st.error("Marche pathologique")

    st.write("---")

    st.write("🧠 Analyse clinique :")
    for m in analyse_marche(p):
        st.write("➡️", m)

# =========================================================
# 📈 EVOLUTION
# =========================================================

elif mode == "📈 Évolution":

    st.subheader("📊 Évolution du patient")

    st.write(f"Jour actuel : J{p['jour']}")

    if st.button("Avancer de 7 jours"):
        evolution_patient(p)

    st.write("État patient :")
    st.write(p)

# =========================================================
# 🎓 ECOS
# =========================================================

elif mode == "🎓 ECOS":

    st.subheader("🎓 Station ECOS kiné")

    rep = st.radio(
        "Quelle est la priorité thérapeutique ?",
        [
            "Renforcement global",
            "Contrôle moteur",
            "Immobilisation"
        ]
    )

    if st.button("Valider réponse"):

        ok, msg = correction_ecos(rep)

        if ok:
            st.success(msg)
        else:
            st.error(msg)

# =========================================================
# 🤖 TUTEUR IA
# =========================================================

elif mode == "🤖 Tuteur":

    st.subheader("🧠 Analyse clinique guidée")

    for line in analyse_clinique(p):
        st.write(line)

# =========================================================
# 🔄 RESET
# =========================================================

if st.button("Reset patient"):
    st.session_state.p = create_patient()
    st.success("Patient réinitialisé")
