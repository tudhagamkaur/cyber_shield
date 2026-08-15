"""
Minimal test: speech and typewriter running at the same time.
Run: py test_voice.py
"""
import pyttsx3
import threading
import time

def typewriter_and_speak(text, rate=175):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", rate)

    # Start printing in a background thread
    def print_text():
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(0.05)
        print()

    t = threading.Thread(target=print_text, daemon=True)
    t.start()

    # Speak on this thread (blocks until done)
    engine.say(text)
    engine.runAndWait()

    # Make sure text thread is also done
    t.join()

print("\n--- TEST START ---\n")
typewriter_and_speak("Welcome, Agent.")
typewriter_and_speak("Today is your first day at CyberShield.")
typewriter_and_speak("Unfortunately, today is not a normal day.")
print("\n--- TEST END ---")
