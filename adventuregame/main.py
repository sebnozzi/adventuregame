
location = "living_room"
command = ""

while command != "quit":

    if location == "living_room":
        print("You are in the living room. The TV is running, showing one of your favourite movies.")
        print("At the distance, you hear somebody knocking at the house door.")
        print("")
        print("Your spouse is watching the movie with you, and shows no intention to move. ")
        print("")
        print("It seems it's up to you to solve the situation, by some sort of previous agreement.")
        print("")
        print("* North: kitchen")
        print("* South: entrance area")
        print("* West: bedroom")
        print("* East: toilet")
        print("")

        while True:
            command = input("What do you do? ")
            print("")
            if command == "go north":
                location = "kitchen"
                break
            elif command == "go south":
                location = "entrance_area"
                break
            elif command == "go west":
                location = "bedroom"
                break
            elif command == "go east":
                location = "toilet"
                break
            elif command == "quit":
                location = ""
                break
            else:
                print("Sorry, don't know how to do that.")

    if location == "kitchen":
        print("You are in the kitchen. The table is already arranged, courtesy of your spouse.")
        print("")
        print("The only thing missing is the food, which will be delivered any time soon now.")
        print("")
        print("That is your part, as agreed.")
        print("")
        print("Until the food arrives there is nothing else for you to do here.")
        print("")
        print("* South: living room")
        print("")

        while True:
            command = input("What do you do? ")
            print("")
            if command == "go south":
                location = "living_room"
                break
            elif command == "quit":
                location = ""
            else:
                print("Sorry, don't know how to do that.")

    if location == "entrance_area":
        print("You are in the entrance area. You can hear the knocks loud now.")
        print("")
        print("At the other side of the door somebody says \"Food delivery!\"")
        print("")
        print("But you realise you don't have your wallet with you, and can't remember where you put it.")
        print("Maybe your spouse knows. It would not hurt to ask.")
        print("")
        print("* North: living room")
        print("* South: the street")
        print("")

        while True:
            command = input("What do you do? ")
            print("")
            if command == "go north":
                location = "living_room"
                break
            elif command == "go south":
                print("You don't want to leave the house. Your favourite movie is running. And you are hungry")
                print("And to get the food delivery you need your wallet.")
            elif command == "quit":
                location = ""
            else:
                print("Sorry, don't know how to do that.")

    if location == "bedroom":
        print("You are in the bedroom. The room is dark.")
        print("")
        print("You know you left somebody important here, but don't remember what.")
        print("")
        print("* East: living room")
        print("")

        while True:
            command = input("What do you do? ")
            print("")
            if command == "go east":
                location = "living_room"
                break
            elif command == "quit":
                location = ""
            else:
                print("Sorry, don't know how to do that.")

    if location == "toilet":
        print("You are in the toilet. You don't need to be here right now.")
        print("")
        print("* West: living room")
        print("")

        while True:
            command = input("What do you do? ")
            print("")
            if command == "go west":
                location = "living_room"
                break
            elif command == "quit":
                location = ""
            else:
                print("Sorry, don't know how to do that.")

print("You quit the game")
