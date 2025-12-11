import streamlit as st
from datetime import datetime
from langdetect import detect

# 🔄 Réinitialisation automatique le 1er du mois
today = datetime.today()
if today.day == 1:
    st.cache_data.clear()
    st.session_state.clear()
    st.success("🔄 PresiScope a été réinitialisé pour le nouveau mois.")

# 🌐 Détection de langue
def detect_language():
    try:
        return detect(st.session_state.get("input_text", "Bonjour"))
    except:
        return "en"

# 🧠 Titre adaptatif
def get_title(president="Donald Trump"):
    return {
        "fr": f"PrésiScope – Analyse adaptative sous {president}",
        "en": f"PresiScope – Adaptive Insight under {president}",
        "ar": f"بريسي سكوب – تحليل رئاسي تحت {president}"
    }.get(lang, f"PresiScope – Adaptive Insight under {president}")

# 🌍 Langue
lang = detect_language()

# 🎨 Interface
st.set_page_config(page_title="PresiScope", page_icon="🇺🇸")

st.markdown(f"# {get_title()}")
st.markdown("---")

# 🧠 Entrée utilisateur
input_text = st.text_area({
    "fr": "Entrez votre question politique ici...",
    "en": "Enter your political question here...",
    "ar": "اكتب سؤالك السياسي هنا..."
}[lang], key="input_text")

# 🔐 Mode admin
if "#admin" in input_text and "@Action26" in input_text:
    st.markdown("## 🔐 Admin Mode Activated")
    st.info("Vous pouvez maintenant accéder aux outils premium, réinitialiser l’app, ou tester les paiements.")
else:
    if input_text:
        st.markdown("### 🤖 Réponse IA (démo)")
        st.write("Cette section affichera une réponse adaptative selon le président en cours, la langue et le ton.")
        st.code("Réponse simulée ici… (à compléter avec une API ou modèle local)")
