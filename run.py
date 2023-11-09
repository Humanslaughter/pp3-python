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

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

generate_ships(computer_board, label2)
generate_ships(player_board, label1)
# Print empty starting boards
print_board(player_guess_board, label2)
print_board(computer_guess_board, label1)
turns = 20
while turns > 0:
    # Player turn
    while True:
        row, column = get_ship_location()
        if player_guess_board[row][column] == '*':
            print("You already guessed that, try again.")
        elif computer_board[row][column] == 'X':
            print('')
            print('===========')
            print('PLAYER HIT!')
            print('===========')
            player_guess_board[row][column] = 'X'
            print_board(player_guess_board, label2)
            turns -= 1
            break
        else:
            print('')
            print('============')
            print('PLAYER MISS!')
            print('============')
            player_guess_board[row][column] = '*'
            print_board(player_guess_board, label2)
            turns -= 1
            break
    if count_hit_ships(player_guess_board) == 5:
        print('')
        print('===========')
        print('PLAYER WON!')
        print('===========')
        break
    # Computer turn
    while True:
        row, column = randint(0,7), randint(0,7)
        while computer_guess_board[row][column] == '*':
            row, column = randint(0,7), randint(0,7)
        if player_board[row][column] == 'X':
            print('=============')
            print('COMPUTER HIT!')
            print('=============')
            computer_guess_board[row][column] = 'X'
            print_board(computer_guess_board, label1)
            break
        else:
            print('==============')
            print('COMPUTER MISS!')
            print('==============')
            computer_guess_board[row][column] = '*'
            print_board(computer_guess_board, label1)
            break
    if count_hit_ships(computer_guess_board) == 5:
        print('')
        print('=============')
        print('COMPUTER WON!')
        print('=============')
        break
    # Turns left until game over
    print(''+str(turns)+' turn(s) left.')
    # 0 turns left
    if turns == 0:
        print('==========')
        print('GAME OVER!')
        print('==========')
        break