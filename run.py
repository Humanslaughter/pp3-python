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
player_board = [['_'] * 8 for x in range(8)]
computer_board = [['_'] * 8 for x in range(8)]
player_guess_board = [['_'] * 8 for x in range(8)]
computer_guess_board = [['_'] * 8 for x in range(8)]

