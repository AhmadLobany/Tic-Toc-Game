def display_board(board):
    row = ['   ', '   ', '   ', '|', '   ',
           '   ', '   ', '|', '   ', '   ', '   ']
    gap = ['___', '___', '___', '|', '___',
           '___', '___', '|', '___', '___', '___']
    gameBoard = [list(row), list(row), list(row), gap, list(row), list(
        row), list(row), gap, list(row), list(row), list(row)]
    i = 1
    j = 1
    current = 1
    while i <= 9:
        while j <= 9:
            gameBoard[i][j] = ' ' + board[current] + ' '
            current += 1
            j += 4
        j = 1
        i += 4
    for i in range(len(row)):
        for j in range(len(row)):
            print(gameBoard[i][j], end="")
            if j == (len(row)-1):
                print('')


def player_input():
    flag = 0
    while flag == 0:
        userInput = input("Please pick a marker 'X' or 'O': ")
        if(userInput == 'x'):
            return 'X'
        if(userInput == 'o'):
            return 'O'
        if(userInput == 'X' or userInput == 'O'):
            return userInput


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark
            or board[7] == board[8] == board[9] == mark):
           return True
    if (board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark
            or board[3] == board[6] == board[9] == mark):
                  return True
    if (board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark):
        return True
    return False


def choose_first():
    import random
    randNum = random.randint(1, 2)
    if(randNum == 1):
        print('Player 1 starts first!/n')
    else:
        print('Player 2 starts first!/n')
    return randNum


def full_board_check(board):
    for x in board:
        if(x == '#'):
            continue
        if(x == ' '):
            return False
    return True


def player_choice(board):
    position = int(input('Please enter a number 1-9: '))
    if(board[position] == ' '):
        return position
    else:
        return -1


def replay():
    ask = input('Would You Want To Play Again? Y/N ')
    if ask == 'y' or ask == 'Y':
        return True
    return False

