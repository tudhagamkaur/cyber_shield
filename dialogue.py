from voice import speak, ORION, NEXUS, SYSTEM
import time
from characters import typewriter

def orion(text):
    print("\n━━━━━━━━━━━━━━━━━━━━━")
    print("📡 Commander Orion")
    print("━━━━━━━━━━━━━━━━━━━━━━━━")
    print("-" * 30)
    typewriter(text, voice=ORION, rate=2)

def nexus(text):
    print("\n━━━━━━━━━━━━")
    print("🤖 NEXUS")
    print("━━━━━━━━━━━━━━")
    typewriter(text, voice=NEXUS, rate=0)
    print("-" * 30)

def system(text):
    print("\n━━━━━━━━━━━━━━━━━━━")
    print("💻 SYSTEM")
    print("━━━━━━━━━━━━━━━━━━━━━")
    typewriter(text, voice=SYSTEM, rate=3)
    print("-" * 30)

def narration(text):
    typewriter(text)