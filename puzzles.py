from player import player
def password_puzzle():
    print("\n===================================")
    print("      PASSWORD VERIFICATION")
    print("===================================")
    print("\nA secure server is locked.")
    print("\nChoose the strongest password:\n")
    print("1. password123")
    print("2. Cyber#7")
    print("3. admin")
    print("4. abc123")
    answer = input("\nYour Choice: ")
    if answer == "2":
        print("\n✔ Access Granted!")
        print("Strong password detected.")
        player["xp"] += 15
        player["inventory"].append("Master Access Card")
    else:
        print("\n✖ Weak Password!")
        print("The server remains locked.")
        player["integrity"] -= 10
    input("\nPress ENTER to continue...")
def binary_puzzle():

     print("\n===================================")
     print("         BINARY DECODER")
     print("===================================")

     print("\nNEXUS has sent a secret message.")
     print("Decode it correctly.\n")

     print("01001000 01101001")

     answer = input("\nWhat does it say? ")

     if answer.lower() == "hi":

        print("\n✔ Correct!")
        print("Message Decoded.")

        player["xp"] += 20
        player["inventory"].append("Binary Decoder")

     else:

        print("\n✖ Incorrect!")
        print("The message was 'Hi'.")

        player["integrity"] -= 10

     input("\nPress ENTER to continue...")