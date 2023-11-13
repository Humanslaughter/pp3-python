# PP3 Python: Battleships

![smartmockups_low19brg](https://github.com/Humanslaughter/pp3-python/assets/122393963/1af3ad63-4c4a-4a95-a54a-8c3b969935bb)

[Play Battleships](https://pp3-python-battleships-1a94bc079202.herokuapp.com/)

How to play:
- The player enters a number between 1 to 8 for the row and a letter between A to H for the column.
- "X" indicates a hit on the board, and a message displaying "a hit!" is shown when a ship is hit.
- "*" indicates a miss on the board with a message displaying "missed!".
- The game is over whenever the player or computer hits all 5 ships or there are no more turns left and the game is over. 

---

## Contents

* [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Features](#future-features)

* [Technologies Used](#technologies-used)
  * [Languages](#languages)

* [Testing](#testing)
  * [Validator Testing](#validator-testing)
  * [Known Bugs & Issues](#known-bugs--issues)

* [Deployment](#deployment)
 	* [Heroku Deployment](#heroku-deployment)
  * [How To Fork](#how-to-fork)
  * [How To Clone](#how-to-clone)

* [Credits](#credits)
  * [Code](#code) 

---

## Features

### Existing Features
- Play against a computer.
- Random generation of ship placement for both the player and computer.
- The ships are hidden until hit, which is indicated by an "X" on the board.
- The board layout is 8x8 with 5 ships on each board and 30 turns.
- You can only enter numbers between 1 and 8 as a row, only letters between A and H as a column, and you cannot leave any input fields empty. If you do, a message will display telling you the input is not valid and to enter a valid one instead.
- Whenever the same combination of rows and columns is guessed multiple times, a message is displayed saying "You've guessed that already, try again!".
- A scoring system that updates each time the player or computer hits a ship.
- A result system that displays if it's a hit/miss, how many turns are left, who's the winner, or if it's a game over.
- Option to restart or quit when the game is over.

![Start 2](https://github.com/Humanslaughter/pp3-python/assets/122393963/b788e857-b7ed-4ded-958a-224af8d5a0d2)
![Skärmbild 2023-11-12 224530](https://github.com/Humanslaughter/pp3-python/assets/122393963/c98f6648-9d1c-4c9c-b7f1-830a8b5c919a)
![Skärmbild 2023-11-12 224614](https://github.com/Humanslaughter/pp3-python/assets/122393963/4ff63fd0-abf6-4d1b-b371-686b145b5da4)
![Skärmbild 2023-11-12 224522](https://github.com/Humanslaughter/pp3-python/assets/122393963/543dbb28-f885-4ab0-80fb-e515a92c61c6)

### Future Features
- The player will be able to pick the ship's location and see the placement on the board while playing.
- Different sizes of ships and boards, different difficulty modes (easy, medium, hard mode).
- Add some colors to the design.
- Multiplayer mode (player vs player).
- Ability to quit the game during an active session.

## Technologies Used

### Languages
- Python.

## Testing
I have manually done these tests:<br>
- Passed the code through the PEP8 linter and confirmed that no problems or errors exist.
- Added error handling on all inputs, to make sure no invalid inputs can be given without a warning.
- Done tests in both my local terminal and the Code Institute Python terminal to ensure that each input and function works as it should. For example, when pressing enter or Q the game restarts or quits.

### Validator Testing
- [PEP8](https://pep8ci.herokuapp.com/)<br>
  No errors.

### Known Bugs & Issues
- Sometimes it takes a second for it to load in everything at the start when you click the run program and it can seem like it has bugged out or something similar, not sure if it's something on my end or if it is the terminal itself. I mostly noticed it while using Dev Tools.
- Sometimes when asking for a row/column and you've put those in it will yet again ask for a row and column. It doesn't happen very often and most of the time it's just one time and then it will go back to working normally again. There were one or two times when it got stuck in an endless loop asking for a row/column, but it fixed itself whenever I clicked 'run program' or refreshed the webpage.

## Deployment
The project was deployed using Code Institute's Python Terminal on Heroku.

### Heroku Deployment

Steps:<br>
1. Clone or Fork this repository [pp3-python](https://github.com/Humanslaughter/pp3-python).
2. Create and/or log in to your account on Heroku.com
3. Click on 'Create new app' from your dashboard.
4. Set the buildbacks to Python and NodeJS (in that exact order).
5. Link the repository to the Heroku app.
6. Click 'Deploy'.

#### How To Fork

Fork the repository:<br>
  1. Log in/sign up to GitHub.
  2. Go to the repository for this project [pp3-python](https://github.com/Humanslaughter/pp3-python).
  3. Click the 'Fork' button in the top right corner.

#### How To Clone

Clone the repository:<br>
  1. Log in/sign up to GitHub.
  2. Go to the repository for this project [pp3-python](https://github.com/Humanslaughter/pp3-python).
  3. Click the code button, select which one you want to clone with (HTTPS, SSH, or GitHub CLI), and copy the link shown.
  4. Open the terminal in a code editor and change the current working directory to a location of your choice to use for the cloned directory.
  5. Type 'git clone' in the terminal, paste the link that you copied in step 3 and then press enter.

## Credits

### Code
- Code Institute for the Python Essentials Template and Python Terminal.
- Followed Code Institute's 'Portfolio Project Scope' README Template that they made for their project called 'ULTIMATE Battleships'.
- Took some tips and inspiration from some of [Knowledge Mavens](https://www.youtube.com/@KnowledgeMavens) tutorials, e.g. [How to Code Battleship in Python - Single Player Game](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=1209s).
