import os, time, random

def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    winner_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    game_over = 0
    replay_request = ""
    red_x = "\033[91mx\033[00m"
    green_o = "\033[92mo\033[00m"
    while(replay_request != "n"):
        while(True): 
            cls()
            Print(board)
            user_input(board, green_o, red_x)
            cls()
            Print(board)
            game_over = winner_position(board, winner_positions, game_over, green_o, red_x)
            if game_over == 1 or game_over == 3:
                if game_over == 1: 
                    print("Congratulations, you won!")
                elif game_over == 3:
                    print("It\'s a tie")
                break
            AI(board, winner_positions, green_o, red_x)
            cls()
            Print(board)
            game_over = winner_position(board, winner_positions, game_over, green_o, red_x)
            if game_over == 2 or game_over == 3:
                if game_over == 2: 
                    print("Game Over! The computer won!")
                if game_over ==3:
                    print("It\'s a tie")
                break
        replay_request = input("Do you want to play another round? (y/n):")
        for x in range(len(board)): 
            board[x] = x 
        game_over = 0


def Print(board):
    dash = "+-+-+-+"
    separator = "|"
    for x in range(len(board)):
        if x == 0:
            print(dash)
        print(f"{separator}{board[x]}", end="")
        if x == 2 or x == 5 or x == 8:
            print("|")
            print(dash)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')  


def user_input(board, green_o, red_x):
    while(True):
        try:
            enter_num = int(input("Please enter the number: "))
        except ValueError:
            print("Use only numbers please!")
            continue
        if enter_num not in board:
            print("Invalid position!")
            continue
        elif board[enter_num] == red_x or board[enter_num] == green_o:
            print("That position is already taken!")
            continue
        else:
            board[enter_num] = red_x
            break


def winner_position(board, winner_positions, game_over, green_o, red_x):
    for x in winner_positions:
        if board[x[0]] == red_x and board[x[1]] == red_x and board[x[2]] == red_x:
            game_over = 1
            break
        if board[x[0]] == green_o and board[x[1]] == green_o and board[x[2]] == green_o:
            game_over = 2
            break
        if board.count(red_x) == 5:
            game_over = 3
    return game_over


def AI(board, winner_positions, green_o, red_x):
    four_corner = [0, 2, 6, 8]
    time.sleep(.500)
    marker = 0
    for x in winner_positions:
        if [board[x[0]], board[x[1]], board[x[2]]].count(green_o) == 2 and any(isinstance(y, int) for y in [board[x[0]], board[x[1]], board[x[2]]]):
            for y in range(len(x)):
                if isinstance(board[x[y]], int) and marker == 0:
                    board[x[y]] = green_o
                    marker = 1
    if marker == 0:
        for x in winner_positions:
            if [board[x[0]], board[x[1]], board[x[2]]].count(red_x) == 2 and any(isinstance(y, int) for y in [board[x[0]], board[x[1]], board[x[2]]]):
                for y in range(len(x)):
                    if isinstance(board[x[y]], int) and marker == 0:
                        board[x[y]] = green_o
                        marker = 1
    if marker == 0: 
        for x in winner_positions:
            if [board[x[0]], board[x[1]], board[x[2]]].count(green_o) == 1 and red_x not in [board[x[0]], board[x[1]], board[x[2]]]:
                for y in range(len(x)):
                    if board[x[y]] != green_o and marker == 0:
                        board[x[y]] = green_o
                        marker = 1
    if marker == 0: 
        while(True):
            if isinstance(board[4], int):
                board[4] = green_o
                break
            random_num = random.randint(0, 3)
            if board[four_corner[random_num]] == red_x or board[random_num] == green_o: 
                continue
            else: 
                board[four_corner[random_num]] = green_o
                break
       

if __name__ == "__main__":
    main()

    

    
    
         


    
    
    
      



  

