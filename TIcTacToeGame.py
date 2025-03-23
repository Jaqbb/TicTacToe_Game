def check_winner(game, symbol):
    for i in range(3):
        if all(game[i][j] == symbol for j in range(3)):
            return True
        if all(game[j][i] == symbol for j in range(3)):
            return True

    if all(game[i][i] == symbol for i in range(3)):
        return True
    if all(game[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def check_tie(game):
    for i in game:
        if " " in i:
            return False
    return True

def TicTacToe():
    end_game = False
    player1 = True
    player2 = False
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    good_choice = ["1","2","3"]
    while not end_game:

        if player1:
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            player1x = input("Wybierz wiersz, gdzie wstawić O: ")
            player1y = input("Wybierz kolumnę, gdzie wstawić O: ")
            if player1x in good_choice and player1y in good_choice:
                player1x = int(player1x)-1
                player1y = int(player1y)-1
                if game[player1x][player1y] == " ":
                    game[player1x][player1y] = "O"
                    player1 = False
                    player2 = True
                else:
                    print("Jest tam już znak")
            else:
                print("wpisz cyfrę!!!")


        if check_winner(game, "O"):
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            print("Gracz 1 (O) wygrywa!")
            end_game = True
        elif check_winner(game, "X"):
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            print("Gracz 2 (X) wygrywa!")
            end_game = True
        elif check_tie(game):
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            print("Remis!")
            end_game = True

        if player2 and not end_game:
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            player2x = input("Wybierz wiersz, gdzie wstawić X: ")
            player2y = input("Wybierz kolumnę, gdzie wstawić X: ")
            if player2x in good_choice and player2y in good_choice:
                player2x = int(player2x)-1
                player2y = int(player2y)-1
                if game[player2x][player2y] == " ":
                    game[player2x][player2y] = "X"
                    player2 = False
                    player1 = True
                else:
                    print("Jest tam już znak")
            else:
                print("wpisz znak!!!")

        if check_winner(game, "O"):
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            print("Gracz 1 (O) wygrywa!")
            end_game = True
        elif check_winner(game, "X"):
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            print("Gracz 2 (X) wygrywa!")
            end_game = True
        elif check_tie(game):
            print(f"{game[0]}\n {game[1]}\n {game[2]}")
            print("Remis!")
            end_game = True




TicTacToe()
