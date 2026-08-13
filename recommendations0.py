def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-Player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommand("poker")
        elif players == "Single-Player":
            recommand("klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommand("Hearts")
        elif players == "Single-Player":
            recommand("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")
            

def recommand(game):
    print("you might like", game)

main()