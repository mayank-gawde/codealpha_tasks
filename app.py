import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException

st.set_page_config(page_title="Lingua — Language Translator", page_icon="🌍", layout="centered")

LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "Portuguese": "pt",
    "Italian": "it",
    "Korean": "ko",
}

st.title("🌍 Lingua")
st.caption("A simple language translation tool built with Python.")
st.divider()

left, right = st.columns(2)
with left:
    source_name = st.selectbox("Translate from", list(LANGUAGES.keys()), index=1)
with right:
    target_name = st.selectbox("Translate to", list(LANGUAGES.keys()), index=3)

source_code = LANGUAGES[source_name]
target_code = LANGUAGES[target_name]

text = st.text_area("Enter your text", placeholder="Type or paste text here...", height=170)

if st.button("✨ Translate", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    elif target_code == "auto":
        st.warning("Please choose a specific target language.")
    elif source_code == target_code:
        st.info("The source and target languages are the same.")
        st.session_state["translation"] = text
    else:
        try:
            translator = GoogleTranslator(source=source_code, target=target_code)
            st.session_state["translation"] = translator.translate(text.strip())
            st.session_state["translation_source"] = source_name
            st.session_state["translation_target"] = target_name
        except LanguageNotSupportedException:
            st.error("That language combination is not supported. Please choose another language.")
        except Exception as exc:
            st.error("Translation could not be completed. Check your internet connection and try again.")
            st.caption(f"Technical detail: {exc}")

if st.session_state.get("translation"):
    st.subheader("Translation")
    st.text_area("Translated text", value=st.session_state["translation"], height=170, key="translated_output")
    st.caption(
        f'{st.session_state.get("translation_source", source_name)} → '
        f'{st.session_state.get("translation_target", target_name)}'
    )
    st.button(
        "📋 Copy tip: select the translated text and press Ctrl+C",
        disabled=True,
        use_container_width=True,
    )

st.divider()
st.caption("Note: This demo uses the deep-translator package and an online translation service. Avoid entering sensitive or confidential text.")
