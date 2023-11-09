from random import randint

# 'X' = ships hit
# '*' = hits missed

# Welcome message
print('=' * 42)
print('            -- BATTLESHIPS --')
print('=' * 42)
print('                 WELCOME!')
print('')
print('           Row: 1-8, Column: A-H')
print('            Ships: 5, Turns: 20')
print('=' * 42)

# Board with generated ships
player_board = [[' '] * 8 for x in range(8)]
computer_board = [[' '] * 8 for x in range(8)]
# Guessing board with ships hidden
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

# Board labels
# Player's board = Computer guesses
label1 = " PLAYER'S BOARD" 
# Computer's board = Player guesses
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

def get_ship_location():
    print('Make your guess.')
    # Enter a row number between 1 to 8
    row = input('Row 1-8: ')
    while row not in '12345678':
        print('Invalid row input, please enter a number between 1-8')
        row = input('Row 1-8: ')
    # Enter a column letter between A to H
    column = input('Column A-H: ').upper()
    while column not in 'ABCDEFGH':
        print('Invalid column input, please enter a letter between A-H')
        column = input('Column A-H: ').upper()
    return int(row) - 1, let_to_num[column]

# Generate random ships for player and computer
def generate_ships(board, label):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = 'X'

