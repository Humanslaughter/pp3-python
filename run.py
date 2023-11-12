from random import randint

# 'X' = ships hit
# '*' = turns missed
# Player's board = The computer's guesses displayed
# Computer's board = The player's guesses displayed

def start_game():
# Welcome message
    print('=' * 42)
    print('-- BATTLESHIPS --'.center(42))
    print('=' * 42)
    print('WELCOME!'.center(42))
    print('')
    print('Row: 1-8, Column: A-H'.center(42))
    print('Ships: 5, Turns: 30'.center(42))
    print('=' * 42)
    
    # Prompt the player to enter their name
    player_name = input('Enter your name: ')

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
    label1 = f"{player_name.upper()}'S BOARD"
    label2 = "COMPUTER'S BOARD"

    # Prints the board
    def print_board(board, label):
        print(f'\n {label}')
        print('-----------------'.center(21))
        print('A B C D E F G H'.center(21))
        row_num = 1
        for row in board:
            print(f"{str(row_num).rjust(2)}|{'|'.join(row)}|")
            row_num += 1

    # Prints empty starter boards for player and computer
    print_board(player_guess_board, label2.center(18))
    print_board(computer_guess_board, label1.center(19))

    # Player guess ship locations on the computer board
    def get_ship_location():
        print('')
        print('Make your guess')
        print('----------------')
    # Player enter a row number between 1 to 8
        row = input('Row 1-8: ')
        while row not in '12345678':
            print('Invalid row input, please enter a number between 1 and 8')
            row = input('Row 1-8: ')
    # Player enter a column letter between A to H
        column = input('Column A-H: ').upper()
        print('----------------')
        while column not in 'ABCDEFGH':
            print('Invalid column input, please enter a letter between A and H')
            column = input('Column A-H: ').upper()
        return int(row) - 1, let_to_num[column]

    # Generates random ships for player and computer
    def generate_ships(board, label):
        for ship in range(5):
            ship_row, ship_column = randint(0,7), randint(0,7)
            while board[ship_row][ship_column] == 'X':
                ship_row, ship_column = get_ship_location()
            board[ship_row][ship_column] = 'X'
    
    # Counts amount of ships that's hit
    def count_hit_ships(board):
        count = 0
        for row in board:
            for column in row:
                if column == 'X':
                    count += 1
        return count
    
    # Generate ships on player and computer board
    generate_ships(computer_board, label2)
    generate_ships(player_board, label1)
    
    # Player and computer results
    player_results = []
    computer_results = []
    # Current player and computer score, updates each time a ship is hit
    player_score = 0
    computer_score = 0
    turns = 30
    while turns > 0:
        # Player guess
        while True:
            row, column = get_ship_location()
            if player_guess_board[row][column] == '*':
                print("You've guessed that already, try again!")
            elif computer_board[row][column] == 'X':
                player_guess_board[row][column] = 'X'
                print_board(player_guess_board, label2.center(18))
                turns -= 1
                player_results.append(f"{player_name.upper()}: A HIT!")
                player_score += 1
                break
            else:
                player_guess_board[row][column] = '*'
                print_board(player_guess_board, label2.center(18))
                turns -= 1
                player_results.append(f"{player_name.upper()}: MISSED!")
                break
            # Player wins
            if count_hit_ships(player_guess_board) == 5:   
                print(f"{player_name.upper()} WON THE GAME!")
                # Restart or quit game
                restart = input('Press Enter to restart, Q to quit: ').upper()
                if restart == '':
                    start_game()
                elif restart == 'Q':
                    print('Thanks for playing!')
                    break
        # Computer guess
        while True:
            row, column = randint(0,7), randint(0,7)
            while computer_guess_board[row][column] == '*':
                row, column = randint(0,7), randint(0,7)
            if player_board[row][column] == 'X':
                computer_guess_board[row][column] = 'X'
                print_board(computer_guess_board, label1.center(19))
                computer_results.append('COMPUTER: A HIT!')
                computer_score += 1
                break
            else:
                computer_guess_board[row][column] = '*'
                print_board(computer_guess_board, label1.center(19))
                computer_results.append('COMPUTER: MISSED!')
                break
            # Computer wins
            if count_hit_ships(computer_guess_board) == 5:
                print('COMPUTER WON THE GAME!')
                # Restart or quit game
                restart = input('Press Enter to restart, Q to quit: ').upper()
                if restart == '':
                    start_game()
                elif restart == 'Q':
                    print('Thanks for playing!')
                    break

        # Displays the result of each guessed turn with hit or miss for player and computer
        print('')
        print('====================')
        for player_result, computer_result in zip(player_results, computer_results):
            print(f" {player_result:<20}")
            print('')
            print(f" {computer_result:<20}")
            print('--------------------')
            # Player and computer score, updates each time a ship is hit
            print(f" {player_name.upper()}: {player_score}")
            print('')
            print(f" COMPUTER: {computer_score}")
            print('--------------------')
            # Turns left
            print(' '+str(turns)+' turn(s) left')
            # No turns left
            if turns == 0:
                print('GAME OVER!')
                restart = input('Press Enter to restart, Q to quit: ').upper()
                if restart == '':
                    start_game()
                elif restart == 'Q':
                    print('Thanks for playing!')
                    break
        print('====================')

        # Clear old result after each turn
        player_results.clear()
        computer_results.clear()


start_game()