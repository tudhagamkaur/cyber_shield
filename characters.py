from voice import speak,ORION,NEXUS
import time

def typewriter(text, speed=0.03, voice=None, rate=170):

    if voice is not None:
        speak(text, voice, rate)   # Speak first

    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)

    print()
def commander_intro():
    typewriter("\n[Incoming Secure Transmission...]")
    time.sleep(1)
    typewriter("\nCommander Orion:")
    typewriter("Welcome,Agent.",voice=ORION,rate=175)
    typewriter("Today is your first day at CyberShield.",voice=ORION,rate=175)
    typewriter("Unfortunately... today is not a normal day.",voice=ORION,rate=175)
    time.sleep(0.3)
    typewriter("Several countries have lost control of their networks.",voice=ORION,rate=175)
    typewriter("Hospitals,banks and airports are under attack.",voice=ORION,rate=175)
    input("\nPress ENTER to continue...")
def nexus_intro():
    print("\n===================================")
    print(" UNKNOWN CONNECTION DETECTED ")
    print("===================================")
    time.sleep(1)
    typewriter("\nConnecting...")
    time.sleep(1)
    typewriter("\nIdentity Confirmed")
    print("""
==============================
        NEXUS
Neural Execution System
==============================
""")
    print("NEXUS:")
    typewriter(" Greetings, Human.",voice=NEXUS,rate=135)
    typewriter(" I have been waiting for you.",voice=NEXUS,rate=135)
    typewriter(" Your species created me...",voice=NEXUS,rate=135)
    typewriter(" Now you fear me.",voice=NEXUS,rate=135)

    input("\nPress ENTER to continue...")