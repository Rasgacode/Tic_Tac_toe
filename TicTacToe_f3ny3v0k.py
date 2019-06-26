import os, time, random

def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    winnerPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    gameOver = 0
    replayRequest = ""
    redX = "\033[91mx\033[00m"
    greenO = "\033[92mo\033[00m"
    while(replayRequest != "n"):
        while(True): 
            cls()
            Print(board)
            userInput(board, greenO, redX)
            cls()
            Print(board)
            gameOver = winnerPosition(board, winnerPositions, gameOver, greenO, redX)
            if gameOver == 1 or gameOver == 3:
                if gameOver == 1: 
                    print("Congratulations, you won!")
                elif gameOver == 3:
                    print("It\'s a tie")
                break
            AI(board, winnerPositions, greenO, redX)
            cls()
            Print(board)
            gameOver = winnerPosition(board, winnerPositions, gameOver, greenO, redX)
            if gameOver == 2 or gameOver == 3:
                if gameOver == 2: 
                    print("Game Over! The computer won!")
                if gameOver ==3:
                    print("It\'s a tie")
                break
        replayRequest = input("Do you want to play another round? (y/n):")
        for x in range(len(board)): 
            board[x] = x 
        gameOver = 0


def Print(board):
    dash = "-"*7
    divider = "|"
    for x in range(len(board)):
        if x == 0:
            print(dash)
        print(divider + str(board[x]), end="")
        if x == 2 or x == 5 or x == 8:
            print("|")
            print(dash)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')  


def userInput(board, greenO, redX):
    while(True):
        try:
            enterNum = int(input("Please enter the number: "))
        except ValueError:
            print("Use only numbers please!")
            continue
        if enterNum not in board:
            print("Invalid position!")
            continue
        elif board[enterNum] == redX or board[enterNum] == greenO:
            print("That position is already taken!")
            continue
        else:
            board[enterNum] = redX
            break


def winnerPosition(board, winnerPositions, gameOver, greenO, redX):
    for x in winnerPositions:
        if board[x[0]] == redX and board[x[1]] == redX and board[x[2]] == redX:
            gameOver = 1
            break
        if board[x[0]] == greenO and board[x[1]] == greenO and board[x[2]] == greenO:
            gameOver = 2
            break
        if board.count(redX) == 5:
            gameOver = 3
    return gameOver


def AI(board, winnerPositions, greenO, redX):
    time.sleep(.500)
    marker = 0
    for x in winnerPositions:
        if [board[x[0]], board[x[1]], board[x[2]]].count(greenO) == 2 and any(isinstance(y, int) for y in [board[x[0]], board[x[1]], board[x[2]]]):
            for y in [board[x[0]], board[x[1]], board[x[2]]]:
                if isinstance(y, int):
                    board[x[y]] = greenO
                    marker = 1
    if marker == 0:
        for x in winnerPositions:
            if [board[x[0]], board[x[1]], board[x[2]]].count(redX) == 2 and any(isinstance(y, int) for y in [board[x[0]], board[x[1]], board[x[2]]]):
                for y in [board[x[0]], board[x[1]], board[x[2]]]:
                    if isinstance(y, int):
                        board[x[y]] = greenO
                        marker = 1
    if marker == 0: 
        for x in winnerPositions:
            if board[x[0]] == greenO and board[x[1]] != redX and board[x[2]] != redX:
                board[x[1]] = greenO
                marker = 1
                break
            elif board[x[1]] == greenO and board[x[0]] != redX and board[x[2]] != redX: 
                board[x[2]] = greenO
                marker = 1
                break
            elif board[x[2]] == greenO and board[x[0]] != redX and board[x[1]] != redX: 
                board[x[0]] = greenO
                marker = 1
                break
    if marker == 0: 
        while(True):
            randomNum = random.randint(0, 8)
            if board[randomNum] == redX or board[randomNum] == greenO: 
                continue
            else: 
                board[randomNum] = greenO
                break
       

if __name__ == "__main__":
    main()

    

    
    
         


    
    
    
      



  

