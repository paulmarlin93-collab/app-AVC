import streamlit as st

# =========================================================
# 🧠 PATIENT AVC (MODÈLE COMPLET)
# =========================================================

def create_patient():
    return {
        "infos": {
            "age": 72,
            "type_avc": "ischémique",
            "cote": "hémiparésie droite",
            "phase": "aigu"
        },

        "deficits": {
            "controle_moteur": 35,
            "force": 40,
            "spasticite": 65,
            "equilibre": 45,
            "coordination": 30
        },

        "patterns": {
            "synergie_flexion_MS": 70,
            "synergie_extension_MI": 75,
            "marche": "circumduction",
            "appui": "instable"
        },

        "fonctionnel": {
            "marche_autonome": False,
            "aide": "canne",
            "risque_chute": True
        },

        "evolution": {
            "jour": 0
        }
    }


# =========================================================
# 📈 STADES AVC
# =========================================================

def get_stade(p):
    j = p["evolution"]["jour"]

    if j < 7:
        return "Phase aiguë (instabilité motrice)"
    elif j < 30:
        return "Phase subaiguë (début récupération)"
    else:
        return "Phase chronique (compensations installées)"


# =========================================================
# 🧠 ANALYSE CLINIQUE KINÉ
# =========================================================

def analyse_clinique(p):

    res = []

    d = p["deficits"]
    pat = p["patterns"]

    if d["controle_moteur"] < 50:
        res.append("↓ contrôle moteur → mouvements en synergie")

    if d["spasticite"] > 60:
        res.append("↑ spasticité → limitation amplitude + posture en extension")

    if d["equilibre"] < 50:
        res.append("↓ équilibre → stratégies de compensation (base élargie)")

    if pat["marche"] == "circumduction":
        res.append("Déficit flexion hanche → circumduction phase oscillante")

    return res


# =========================================================
# 🧠 STRATÉGIES KINÉ
# =========================================================

def strategies_kine(p):

    s = []
    d = p["deficits"]

    if d["controle_moteur"] < 50:
        s.append("Facilitation contrôle moteur (neurofacilitation / Bobath)")

    if d["spasticite"] > 60:
        s.append("Inhibition spasticité + étirements prolongés")

    if d["equilibre"] < 50:
        s.append("Travail transferts de poids + équilibre assis/debout")

    if d["force"] < 50:
        s.append("Renforcement fonctionnel progressif")

    return s


# =========================================================
# 📈 EVOLUTION
# =========================================================

def evolution_patient(p):

    p["evolution"]["jour"] += 7

    p["deficits"]["controle_moteur"] += 2
    p["deficits"]["equilibre"] += 3
    p["deficits"]["spasticite"] -= 2

    return p


# =========================================================
# 🎓 ECOS
# =========================================================

def correction_ecos(rep):

    if rep == "Contrôle moteur":
        return True, "✔ Bonne réponse kinésithérapique"
    return False, "❌ Réponse incomplète"


# =========================================================
# 🖥️ INTERFACE
# =========================================================

st.title("🧠 Simulateur AVC kiné - Version clinique avancée")

if "p" not in st.session_state:
    st.session_state.p = create_patient()

p = st.session_state.p

mode = st.selectbox(
    "Module clinique",
    ["🦶 Marche", "📈 Évolution", "🎓 ECOS", "🤖 Analyse"]
)

# =========================================================
# 🦶 MARCHE
# =========================================================

if mode == "🦶 Marche":

    st.subheader("🚶 Marche pathologique AVC (visualisation)")

    score = (p["deficits"]["controle_moteur"] + p["deficits"]["equilibre"]) / 2

    st.write("Score marche :", int(score))

    # ---------------- VISUEL SIMPLE ----------------
    step = st.slider("Phase de marche (0 = appui / 1 = oscillant)", 0, 1, 0)

    # logique AVC
    if p["patterns"]["marche"] == "circumduction":

        if step == 0:
            st.write("🦶➡️🦶  Appui : instable, extension dominante")
            st.write("Tronc : légère inclinaison")
        else:
            st.write("🦶↺     Oscillation : circumduction du MI")
            st.write("Genou : flexion réduite")

    # bras
    if p["patterns"]["synergie_flexion_MS"] > 60:
        st.write("💪 Bras : absence de balancement, flexion en synergie")

    # classification
    if score > 70:
        st.success("Marche fonctionnelle proche normale")
    elif score > 50:
        st.warning("Marche avec compensations visibles")
    else:
        st.error("Marche pathologique sévère")

    st.write("---")

    st.write("🧠 Lecture kinésithérapique :")

    for a in analyse_clinique(p):
        st.write("➡️", a)


# =========================================================
# 📈 EVOLUTION
# =========================================================

elif mode == "📈 Évolution":

    st.subheader("📊 Évolution du patient")

    st.write(f"Jour : J{p['evolution']['jour']}")
    st.write("Phase :", get_stade(p))

    if st.button("Avancer de 7 jours"):
        evolution_patient(p)

    st.write(p)


# =========================================================
# 🎓 ECOS
# =========================================================

elif mode == "🎓 ECOS":

    st.subheader("🎓 Station clinique")

    rep = st.radio(
        "Priorité thérapeutique ?",
        [
            "Renforcement global",
            "Contrôle moteur",
            "Immobilisation"
        ]
    )

    if st.button("Valider"):

        ok, msg = correction_ecos(rep)

        if ok:
            st.success(msg)
        else:
            st.error(msg)


# =========================================================
# 🤖 ANALYSE GLOBALE
# =========================================================

elif mode == "🤖 Analyse":

    st.subheader("🧠 Synthèse clinique AVC")

    st.write("### Infos patient")
    st.write(p["infos"])

    st.write("### Déficits")
    st.write(p["deficits"])

    st.write("### Patterns moteurs")
    st.write(p["patterns"])

    st.write("### Analyse")
    for a in analyse_clinique(p):
        st.write("➡️", a)

    st.write("### Stratégies")
    for s in strategies_kine(p):
        st.write("✔", s)


# =========================================================
# RESET
# =========================================================

if st.button("Reset patient"):
    st.session_state.p = create_patient()
    st.success("Patient réinitialisé")
