from voice import speak,ORION,NEXUS,SYSTEM
import time
from characters import typewriter

def orion(text):
    print("\n━━━━━━━━━━━━━━━━━━━━━")
    print("📡 Commander Orion")
    print("━━━━━━━━━━━━━━━━━━━━━━━━")
    print("-" * 30)
    typewriter(text,voice=ORION,rate=175)
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.03)

    print()

def nexus(text):
    print("\n━━━━━━━━━━━━")
    print("🤖 NEXUS")
    print("━━━━━━━━━━━━━━")
    typewriter(text,voice=NEXUS,rate=135)
    print("-" * 30)

    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.04)

    print()

def system(text):
    print("\n━━━━━━━━━━━━━━━━━━━")
    print("💻 SYSTEM")
    print("━━━━━━━━━━━━━━━━━━━━━")
    typewriter(text,voice=SYSTEM,rate=200)
    print("-" * 30)

    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.02)

    print()

def narration(text):
    typewriter(text)