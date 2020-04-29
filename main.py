from functions import *

print('Welcome to Tic Tac Toe!\n')

while True:
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(board)
    turn = choose_first()
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        if turn == 1:
            print('** Turn Of Player 1 **')
        else:
            print('** Turn Of Player 2 **')
        mark = player_input()
        pos = player_choice(board)
        if pos == -1:
            print("It is not a free position! Turn moves to the other player... ")
        else:
            place_marker(board, mark, pos)
            print('\n'*100)
            display_board(board)
            if win_check(board, mark):
                print(f"Player {turn} Wins! Congrats ...")
                break
            if(full_board_check(board)):
                print("GAME OVER - No One Won")
                break
        if turn == 1:
            turn = 2
        else:
            turn = 1

    if not replay():
        break
