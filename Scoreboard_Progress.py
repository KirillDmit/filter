from statistics import mean

players = int(input("How many players are there?"))
if players == 1:
    player1_name = input("Enter your name: ")
else:
    player1_name = input("Enter name for player 1: ")
    player2_name = input("Enter name for player 2: ")

while True:
    try:
        game_score = int(input("Please choose the game, enter 301 or 501: "))
        if game_score in [301, 501]:
            print("OK!")
            break
        else:
            print("Incorrect number for the game score")


