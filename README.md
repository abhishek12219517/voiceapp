🎙️ Streamlit Voice-to-Text Application
📋 Overview
This Voice-to-Text application enables users to convert speech into text using their microphone. Built with Streamlit and SpeechRecognition, it leverages the Google Web Speech API to process voice input and display recognized text in real-time.

⚙️ Features
✅ 1. Functionality
🎧 Voice Recording:

A user-friendly button initiates voice recording.
Captures audio input from the user's microphone.
Displays a status indicator (e.g., "Listening...") while recording.
📝 Speech Recognition:

Converts captured audio into text using SpeechRecognition.
Displays recognized text directly within the application.
⚠️ Error Handling:

Handles cases where speech is unclear (sr.UnknownValueError).
Manages API errors and connectivity issues (sr.RequestError).
Provides clear and informative error messages to users.
💡 User Interface (UI):

Built with Streamlit for a clean and simple interface.
Displays an intuitive title ("Voice to Text") and a clear recording button.
Recognized text appears in a readable format.
Error messages are prominently displayed when needed.
🌟 2. Optional Features (For Future Enhancements)
Multi-language speech recognition support.
Audio waveform visualization during recording.
Option to save recognized text to a file.
Dark mode or customizable UI themes.
