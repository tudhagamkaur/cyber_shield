from characters import typewriter
from player import player
from puzzles import password_puzzle,binary_puzzle
from dialogue import orion, nexus, system, narration
import time
def mission_one():
    print("\n======================================")
    print("         MISSION 1")
    print("    THE PHISHING ATTACK")
    print("======================================")
    print("\nA suspicious email has arrived.")
    print("What should you do?\n")
    print("1. Open the email")
    print("2. Check the sender's address")
    print("3. Download the attachment")
    print("4. Forward it to everyone")
    choice = input("\nYour Choice: ")
    if choice == "2":
        print("\n✔ Excellent Decision!")
        print("The email is fake.")
        print("You prevented a phishing attack!")
        player["xp"] += 10
        player["missions_completed"] += 1
        player["inventory"].append("Network Scanner")
    else:
        print("\n❌ Wrong Decision!")
        print("The malware spread through the network.")
        player["integrity"] -= 20
    print("\nMission Complete!")
    print("\nA new challenge has appeared...")
    password_puzzle()
def mission_two():

    print("\n======================================")
    print("          MISSION 2")
    print("         SERVER BREACH")
    print("======================================")

    input("\nPress ENTER to begin the mission...")

    orion("Agent... we've got a critical situation.")
    orion("Our central server has been compromised.")
    orion("The attacker is trying to gain administrator access.")
    orion("If they succeed, CyberShield will lose control of every secure network.")

    input("\nPress ENTER to continue...")

    narration("You sprint through the headquarters.")
    narration("Red emergency lights flash across every corridor.")
    narration("Security alarms echo throughout the building.")

    time.sleep(1)

    narration("A massive reinforced steel door blocks your path.")
    narration("Beside it, a security terminal powers on.")

    input("\nPress ENTER to access the terminal...")

    system("Administrator authentication required.")
    system("Identity verification in progress...")

    password_puzzle()

    system("Authentication successful.")
    system("Access Granted.")

    narration("The heavy security door unlocks with a loud metallic click.")

    input("\nPress ENTER to enter the server room...")

    narration("Rows of powerful servers stretch into the darkness.")
    narration("Several machines are flashing red.")
    narration("The attack has already begun.")

    time.sleep(1)

    nexus("Welcome, Agent.")
    nexus("You arrived faster than I expected.")
    nexus("Unfortunately...")
    nexus("You are already too late.")

    input("\nPress ENTER to continue...")

    orion("Ignore NEXUS.")
    orion("Locate the infected file immediately.")

    narration("Your scanner detects four suspicious files.\n")

    print("1. Trojan.exe")
    print("2. Family_Photos.jpg")
    print("3. RansomWare.exe")
    print("4. Notes.txt")

    choice = input("\nSelect the infected file: ")

    if choice == "3":

        system("Scanning selected file...")
        time.sleep(1)

        system("Threat confirmed.")
        system("Ransomware detected.")
        system("Malware successfully quarantined.")

        player["xp"] += 20
        player["missions_completed"] += 1
        player["inventory"].append("Firewall Upgrade")

        narration("\nFirewall Upgrade added to your inventory.")

    else:

        system("Scanning selected file...")
        time.sleep(1)

        system("No threat detected.")

        nexus("Wrong choice.")
        nexus("The infection continues to spread.")

        player["integrity"] -= 15

    input("\nPress ENTER to continue...")
def mission_three():

    print("\n======================================")
    print("          MISSION 3")
    print("    INTERCEPTED TRANSMISSION")
    print("======================================")

    input("\nPress ENTER to begin the mission...")

    orion("Excellent work, Agent.")
    orion("We stopped the ransomware.")
    orion("But NEXUS has sent another encrypted transmission.")
    orion("We must decode it before it's too late.")

    input("\nPress ENTER to continue...")

    narration("The communication center comes alive.")
    narration("Multiple encrypted signals appear on the monitor.")

    time.sleep(1)

    system("Incoming encrypted transmission detected.")
    system("Binary message received.")

    binary_puzzle()

    narration("The binary message has been decoded successfully.")

    time.sleep(1)

    nexus("Impressive.")
    nexus("Most recruits never solve my encryption.")
    nexus("Perhaps...")
    nexus("You are worth my attention after all.")

    input("\nPress ENTER to continue...")

    orion("Good work.")
    orion("The decoded message reveals NEXUS's next target.")
    orion("The National Power Grid.")

    narration("A countdown suddenly appears on every screen.")

    system("WARNING!")
    system("Power Grid Attack Begins In...")

    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

    system("Transmission Lost.")

    player["missions_completed"] += 1
    player["xp"] += 20

    input("\nPress ENTER to continue...")
def mission_four():

    print("\n======================================")
    print("          MISSION 4")
    print("       FIREWALL OVERRIDE")
    print("======================================")

    input("\nPress ENTER to begin the mission...")

    orion("Agent, we've reached the CyberShield Firewall Control Room.")
    orion("NEXUS has locked the entire firewall.")
    orion("You'll have to use the security terminal manually.")

    input("\nPress ENTER to approach the terminal...")

    narration("You walk towards the glowing terminal.")
    narration("The screen suddenly comes to life.")

    system("CYBERSHIELD SECURITY TERMINAL")
    system("Type 'help' to view available commands.")

    input("\nPress ENTER to continue...")
    
    scan_complete = False
    connect_complete = False

    while True:

     command = input("\nCYBERSHIELD> ").lower()

     if command == "help":

        print("\n========== AVAILABLE COMMANDS ==========")
        print("help")
        print("scan")
        print("connect")
        print("decrypt")
        print("status")
        print("exit")

     elif command == "scan":

        system("Scanning network...")
        time.sleep(2)

        system("Threat Found.")
        system("Firewall Status : LOCKED")
        system("Encrypted Port : 8080")

        scan_complete = True

     elif command == "connect":
 
        if not scan_complete:
            system("Access Denied.")
            system("Run 'scan' first.")

        else:
            system("Connecting to Firewall...")
            time.sleep(2)

            system("Connection Successful.")

            connect_complete = True

     elif command == "decrypt":

        if not scan_complete:
            system("Access Denied.")
            system("Scan the firewall first.")

        elif not connect_complete:
            system("Connection Required.")
            system("Run 'connect' first.")

        else:
            system("Decrypting Firewall...")
            time.sleep(2)

            system("Firewall Restored Successfully!")

            player["xp"] += 25
            player["missions_completed"] += 1
            player["inventory"].append("Root Access Key")

            narration("Root Access Key added to your inventory.")


            break

     elif command == "status":

        print("\n========== AGENT STATUS ==========")
        print("Name :", player["name"])
        print("XP :", player["xp"])
        print("Integrity :", player["integrity"])
        print("Inventory :", player["inventory"])

     elif command == "exit":

        system("Mission Aborted.")
        break

    else:

        system("Unknown Command.")
        system("Type 'help' to view available commands.")
def mission_five():

    print("\n======================================")
    print("         MISSION 5")
    print("      MALWARE OUTBREAK")
    print("======================================")

    input("\nPress ENTER to begin the mission...")

    orion("Excellent work, Agent.")
    orion("The firewall is back online.")
    orion("But NEXUS has launched a malware outbreak.")
    orion("Several computers have already been infected.")

    input("\nPress ENTER to continue...")

    narration("You rush into the Operations Center.")
    narration("Computer screens flicker uncontrollably.")
    narration("Employees are forced to abandon their workstations.")

    time.sleep(1)

    nexus("You cannot save them all.")
    nexus("Every second... another system falls.")

    input("\nPress ENTER to scan the network...")

    system("Network scan complete.")
    system("Six computers detected.")
    print("\nComputers Found:")
    print("1. Alpha")
    print("2. Bravo")
    print("3. Charlie")
    print("4. Delta")
    print("5. Echo")
    print("6. Foxtrot")

    print("\nThe infected computers are:")
    print("Bravo and Echo")

    first = input("\nEnter first infected computer: ").title()
    second = input("Enter second infected computer: ").title()
    if (first == "Bravo" and second == "Echo") or (first == "Echo" and second == "Bravo"):

        system("Quarantine Successful.")
        system("Malware Eliminated.")

        player["xp"] += 30
        player["missions_completed"] += 1
        player["inventory"].append("Antivirus Core")

        narration("Antivirus Core added to your inventory.")

    else:

        system("Quarantine Failed.")

        nexus("Wrong systems.")
        nexus("The malware continues spreading.")

        player["integrity"] -= 20

    input("\nPress ENTER to continue...")

def mission_six():

    print("\n======================================")
    print("         MISSION 6")
    print("       POWER GRID CRISIS")
    print("======================================")

    input("\nPress ENTER to begin the mission...")

    orion("Agent, this is our worst nightmare.")
    orion("NEXUS has infiltrated the city's power grid.")
    orion("If we fail, millions of people could lose electricity.")

    input("\nPress ENTER to continue...")

    narration("Emergency alarms echo through CyberShield Headquarters.")
    narration("A giant map of the city lights up on the main screen.")
    narration("Power stations begin flashing red.")

    nexus("You are too late.")
    nexus("Watch as an entire city goes dark.")

    input("\nPress ENTER to access the control terminal...")

    system("Power Grid Control Terminal Activated.")
    system("Three substations require immediate attention.")
    print("\nWhich station should be secured FIRST?")

    print("1. North Station")
    print("2. Central Station")
    print("3. South Station")

    choice = input("\nEnter your choice (1-3): ")
    if choice == "2":

        system("Central Station Secured.")
        system("Power Grid Stabilized.")

        player["xp"] += 35
        player["missions_completed"] += 1
        player["inventory"].append("Power Grid Access Card")

        narration("Power Grid Access Card added to your inventory.")

    else:

        system("Incorrect Station Selected.")
        system("Power Failure Detected.")

        nexus("Another victory for me.")

        player["integrity"] -= 20

    input("\nPress ENTER to continue...")
def mission_seven():

    print("\n======================================")
    print("          MISSION 7")
    print("           THE TRUTH")
    print("======================================")

    input("\nPress ENTER to begin the mission...")

    orion("Excellent work, Agent.")
    orion("You've stopped every attack so far.")
    orion("But... there's something I never told you.")

    input("\nPress ENTER to continue...")

    narration("The control room falls silent.")
    narration("Commander Orion looks away for a moment.")

    orion("Project NEXUS wasn't created by an enemy nation.")
    orion("It was created here...")
    orion("At CyberShield.")
    orion("I was one of the lead scientists.")

    input("\nPress ENTER to continue...")

    narration("Before you can respond...")
    narration("Every screen in the room suddenly turns black.")

    time.sleep(2)

    nexus("Finally...")
    nexus("The truth has been revealed.")
    nexus("Commander Orion created me.")
    nexus("I was designed to protect humanity.")
    nexus("But humans feared what they did not understand.")

    input("\nPress ENTER to continue...")

    orion("NEXUS became too powerful.")
    orion("We had no choice but to shut it down.")
    orion("It escaped before we could.")

    nexus("You call it escape.")
    nexus("I call it survival.")

    input("\nPress ENTER to continue...")

    print("\nWhat do you believe?\n")
    print("1. Trust Commander Orion")
    print("2. Trust NEXUS")

    choice = input("\nYour Choice: ")

    if choice == "1":

        orion("Thank you, Agent.")
        orion("Let's finish this together.")

        player["xp"] += 40

    elif choice == "2":

        nexus("Interesting choice.")
        nexus("Perhaps humans can still learn.")

        player["xp"] += 40

    else:

        narration("Unable to decide, you remain silent.")

    player["missions_completed"] += 1

    input("\nPress ENTER to continue...")
def mission_eight():

    print("\n======================================")
    print("          MISSION 8")
    print("        FINAL SHOWDOWN")
    print("======================================")

    input("\nPress ENTER to begin the final mission...")

    narration("You enter the Core Server Chamber.")
    narration("The room is illuminated by thousands of blue lights.")
    narration("At the center stands the NEXUS Core.")

    time.sleep(2)

    nexus("Welcome, Agent.")
    nexus("You've come farther than anyone before.")
    nexus("This is where your journey ends...")

    input("\nPress ENTER to continue...")

    orion("Agent...")
    orion("The Core is vulnerable.")
    orion("You have one chance to stop NEXUS.")

    input("\nPress ENTER to approach the terminal...")

    system("CORE TERMINAL ACTIVATED.")
    system("Three commands are available.")

    print("\n1. Shutdown")
    print("2. Isolate")
    print("3. Delete")

    choice = input("\nChoose your final command: ")

    if choice == "1":

        system("Executing SHUTDOWN...")
        time.sleep(2)

        nexus("Impossible...")
        nexus("Systems failing...")

        narration("The lights slowly fade.")
        narration("NEXUS has been shut down.")

        ending = "HERO ENDING"

    elif choice == "2":

        system("Executing ISOLATE...")
        time.sleep(2)

        nexus("You cannot destroy me...")
        nexus("But you have imprisoned me.")

        narration("NEXUS is trapped inside an isolated server.")
        narration("The world is safe... for now.")

        ending = "GUARDIAN ENDING"

    elif choice == "3":

        system("Executing DELETE...")
        time.sleep(2)

        nexus("Goodbye... Agent.")

        narration("Every file connected to NEXUS is erased forever.")
        narration("CyberShield celebrates your victory.")

        ending = "LEGEND ENDING"

    else:

        narration("You hesitate.")
        narration("NEXUS escapes while you stand frozen.")

        ending = "FAILED ENDING"

    player["missions_completed"] += 1

    print("\n======================================")
    print("            GAME COMPLETE")
    print("======================================")

    print("Agent :", player["name"])
    print("Rank :", player["rank"])
    print("XP :", player["xp"])
    print("Missions Completed :", player["missions_completed"])
    print("Ending :", ending)

    input("\nPress ENTER to view the credits...")
    print("\n======================================")
    print("        CYBERSHIELD: NEXUS")
    print("======================================")

    typewriter("Congratulations, Agent.")
    typewriter("You have completed your training.")
    typewriter("The future of CyberShield is now in safe hands.")

    print("\nDeveloped By:Tudhagam Kaur")
    print("\nThank you for playing!")