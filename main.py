import streamlit as st
import speech_recognition as sr
import tempfile
import os

st.title("Voice to Text")

# Initialize recognizer class
r = sr.Recognizer()

# Create a temporary directory to save audio files
temp_dir = tempfile.mkdtemp()

# Function to save recorded audio to a file
def save_audio_file(audio):
    audio_file = os.path.join(temp_dir, "audio.wav")
    with open(audio_file, "wb") as f:
        f.write(audio.get_wav_data())
    return audio_file

# Function to recognize speech and return the text
def recognize_speech(audio):
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

# Streamlit button to start recording
if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("Listening... Please speak into the microphone.")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise before listening
        try:
            # Record audio with a timeout of 10 seconds
            audio = r.listen(source, timeout=10)
            st.write("Processing...")
            audio_file = save_audio_file(audio)
            recognized_text = recognize_speech(audio)
            
            if recognized_text:
                st.write("Recognized Text:")
                st.write(recognized_text)
                st.write(f"Audio saved as: {audio_file}")
            else:
                st.error("Sorry, could not understand the audio.")
        except sr.WaitTimeoutError:
            st.error("No audio detected within the time limit.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

