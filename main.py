import streamlit as st
import speech_recognition as sr

st.title("Voice to Text")

r = sr.Recognizer()

if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.write("Recognized Text:")
        st.write(text)
    except sr.UnknownValueError:
        st.error("Could not understand audio")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")