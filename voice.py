import pyttsx3
import threading

voices = pyttsx3.init().getProperty("voices")

ORION = voices[0].id
NEXUS = voices[1].id
SYSTEM = voices[2].id

def speak(text, voice_id, rate=170):
    engine = pyttsx3.init()      # New engine every call
    engine.setProperty("voice", voice_id)
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak_background(text, voice_id, rate=170):
    threading.Thread(
        target=speak,
        args=(text, voice_id, rate),
        daemon=True
    ).start()