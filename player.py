# ============================
# PLAYER DATA
# ============================
player = {
    "name": "",
    "rank": "Recruit",
    "xp": 0,
    "integrity": 100,
    "inventory": [],
    "missions_completed": 0
}
def create_player():
    print("\n========== AGENT REGISTRATION ==========\n")
    player["name"] = input("Enter your Agent Name: ")
    print("\nChoose Difficulty")
    print("1. Recruit")
    print("2. Analyst")
    print("3. Cyber Expert")
    choice = input("\nChoice: ")
    if choice == "1":
        player["integrity"] = 120
    elif choice == "2":
        player["integrity"] = 100
    elif choice == "3":
        player["integrity"] = 80
    else:
        print("Invalid choice!")
        print("Recruit selected by default.")
        player["integrity"] = 120
    print("\nRegistration Complete!\n")
    return player
def show_status():
    print("\n==============================")
    print("Agent :", player["name"])
    print("Rank  :", player["rank"])
    print("XP    :", player["xp"])
    print("Integrity :", player["integrity"])
    print("Inventory :", player["inventory"])
    print("==============================")
def update_rank():

    if player["xp"] >= 150:
        player["rank"] = "Cyber Guardian"

    elif player["xp"] >= 120:
        player["rank"] = "Elite Agent"

    elif player["xp"] >= 80:
        player["rank"] = "Senior Agent"

    elif player["xp"] >= 40:
        player["rank"] = "Junior Agent"

    else:
        player["rank"] = "Recruit"