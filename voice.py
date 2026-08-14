"""
Voice module using Windows SAPI directly via win32com.
Avoids all pyttsx3 singleton/threading issues.
"""
import win32com.client
import threading
import time

# Get available voices once at startup
_sapi = win32com.client.Dispatch("SAPI.SpVoice")
_all_voices = _sapi.GetVoices()

# Assign voice tokens by index (safely)
_voice_count = _all_voices.Count
ORION  = _all_voices.Item(0) if _voice_count > 0 else None
NEXUS  = _all_voices.Item(1) if _voice_count > 1 else _all_voices.Item(0)
SYSTEM = _all_voices.Item(2) if _voice_count > 2 else _all_voices.Item(0)

def speak(text, voice_token, rate=2):
    """
    Speak text while typewriter-printing it simultaneously.
    Creates a fresh SAPI SpVoice object each call — no singleton issues.
    rate: SAPI rate scale -10 (slowest) to 10 (fastest). Default 2 = slightly fast.
    """
    def print_text():
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(0.04)
        print()

    # Start text printing in background
    t = threading.Thread(target=print_text, daemon=True)
    t.start()

    # Fresh SAPI object every call — completely avoids singleton problem
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    if voice_token is not None:
        speaker.Voice = voice_token
    speaker.Rate = rate
    speaker.Speak(text)   # Blocking by default

    # Ensure text thread finishes too
    t.join()