import os
import time
from characters import commander_intro, nexus_intro
from player import create_player, show_status,update_rank
from missions import mission_one,mission_two,mission_three, mission_four, mission_five , mission_six,mission_seven,mission_eight
# ==============================
# Utility Functions
# =============================
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def typewriter(text, speed=0.03):
     for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)
     print()
def loading_bar():
     print("\nInitializing CyberShield Terminal...\n")

     for i in range(0, 101, 5):
        bar = "█" * (i // 5)
        print(f"\rLoading: [{bar:<20}] {i}%", end="")
        time.sleep(0.12)
        print("\n")
# ==============================
# Title Screen
# ==============================
def title_screen():
    clear_screen()
    print(r"""
========================================================
   ██████╗██╗   ██╗██████╗ ███████╗██████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
========================================================
          CYBERSHIELD TERMINAL v1.0
========================================================
""")
    loading_bar()
    typewriter("Connecting to CyberShield Headquarters...")
    time.sleep(1)
    typewriter("Secure connection established.")
    time.sleep(1)
# ==============================
# Main Menu
# ==============================
def main_menu():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Start Mission")
        print("2. Load Mission")
        print("3. Credits")
        print("4.instructions")
        print("5. Exit")
        choice = input("\nSelect an option: ")
        if choice == "1":
            typewriter("\nMission starting...")
            player = create_player()
            commander_intro()
            nexus_intro()
            mission_one()
            mission_two()
            mission_three()
            mission_four()
            mission_five()
            mission_six()
            mission_seven()
            mission_eight()
            update_rank()
            show_status()
            break;
        elif choice == "2":
            typewriter("\nLoad feature coming soon...")
            input("\nPress Enter to continue...")
            clear_screen()
            title_screen()
        elif choice == "3":
            print("\n==============================")
            print("CyberShield: The Rogue AI Incident")
            print("Developed by: Tudhagam Kaur")
            print("==============================")
            input("\nPress Enter to continue...")
            clear_screen()
            title_screen()
        elif choice == "4":

            print("\n======================================")
            print("          INSTRUCTIONS")
            print("======================================")

            print("""
         Welcome, Agent!

         • Press ENTER whenever prompted.
         • Solve puzzles to complete missions.
         • Type terminal commands exactly as shown.
         • Wrong choices may reduce your Integrity.
         • Collect rewards and inventory items.
         • Complete all 8 missions to defeat NEXUS.

         Good Luck,Agent!
         """)

            input("Press ENTER to return to the Main Menu...")
        elif choice == "5":
            typewriter("\nGoodbye, Agent.")
            exit()
        else:
            print("\nInvalid choice. Try again.")
# ==============================
# Main Program
# ==============================
title_screen()
main_menu()
