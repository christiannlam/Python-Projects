# Tic tac toe!
def print_board(board):
    #Column Counter
    colCount = 0
    print("- 0 1 2")
    for r in board:
        #Prints Column Index number
        print(colCount, end=" ")
        # Increments column counter
        colCount += 1
        for c in r:
            if c == 0:
                print(".", end=" ")
            elif c == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

def is_valid(r, c, board):
    ## If input is out of bound between 0 and 2
    if r > 2 or r < 0 or c > 2 or c < 0:
        return False
    if board[r][c] == 0 :
        return True

def is_winner(board):
    ## 8 winning methods of tic tac toe
    if board[0][0] == board[0][1] == board[0][2] != 0:
        return True
    elif board[0][0] == board[1][0] == board[2][0] != 0:
        return True
    elif board[0][1] == board[1][1] == board[2][1] != 0:
        return True
    elif board[0][2] == board[1][2] == board[2][2] != 0:
        return True
    elif board[1][0] == board[1][1] == board[1][2] != 0:
        return True
    elif board[2][0] == board[2][1] == board[2][2] != 0:
        return True
    elif board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return True

def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current = 1
    # X Starts Off
    print("X's Turn")
    for i in range(9):
        print_board(board)
        if is_winner(board) == True:
            break
        r = int(input("Give Row: "))
        c = int(input("Give Column: "))
        ## If Valid method returns False
        while is_valid(r, c, board) == False:
            r = int(input("Give Row: "))
            c = int(input("Give Column: "))
        board[r][c] = current
        if current == 1:
            current = 2
            ## If Current becomes 2 0's Turn
            print("\nO's Turn")
        else:
            current = 1
            ## Current 1 = Player 1
            print("\nX's Turn")
main()
