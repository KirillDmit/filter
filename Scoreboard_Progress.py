from statistics import mean

players = int(input("How many players are there?"))
if players == 1:
    player1_name = input("Enter your name: ")
else:
    player1_name = input("Enter name for player 1: ")
    player2_name = input("Enter name for player 2: ")

while True:
    try:
        game_score = int(input("Choose the game, enter 301 or 501: "))
        if game_score in [301, 501]:
            print("OK!")
            break
        else:
            print("Incorrect number for the game score")
    except ValueError:
        print("Enter a number for the game score, either 301 or 501")

player_avg = []
while game_score > 0:
    player_score = int(input("Enter player score:"))
    player_avg.append(player_score)
    game_score -= player_score
    print(str(game_score) + " remaining")

if game_score <= 0:
    avg = round(mean(player_avg))
    print(f"Average for this game was {avg}")




