from random import randint

# Welcome message
print('=' * 42)
print('            -- BATTLESHIPS --')
print('=' * 42)
print('                 WELCOME!')
print('')
print('           Row: 1-8, Column: A-H')
print('            Ships: 5, Turns: 10')
print('=' * 42)

# Player and computer board
player_board = [[' '] * 8 for x in range(8)]
computer_board = [[' '] * 8 for x in range(8)]
player_guess_board = [[' '] * 8 for x in range(8)]
computer_guess_board = [[' '] * 8 for x in range(8)]

let_to_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# Label for the player and computer board
label1 = " PLAYER'S BOARD"
label2 = "COMPUTER'S BOARD"

def print_board(board, label):
    print(f'\n {label}')
    print(' -----------------')
    print('  A B C D E F G H')
    row_num = 1
    for row in board:
        print(f"{row_num}|{'|'.join(row)}|")
        row_num += 1
    print('')

