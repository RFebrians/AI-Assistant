import streamlit as st
import pyttsx3
import time

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Text-to-speech with Python.")

speed, input = (
    st.slider("Select speed", min_value=100, max_value=1000),
    st.text_area(
        "Enter text here", value="The quick brown fox jumps over the lazy dog."
    ),
)

if st.button("Start text-to-speech"):
    with st.spinner("Starting..."):
        time.sleep(1)
    engine = pyttsx3.init()
    engine.setProperty("rate", speed)
    engine.say(input)
    st.success("Started!")
    engine.runAndWait()
