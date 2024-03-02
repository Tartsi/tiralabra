# Implementation Report

- ChatGPT 4 was utilized for information retrieval during this project

### General Structure

- A terminal operated Gomoku game played on a 20x20 game board. AI-opponent in the game utilizes Minimax that is optimized with Alpha-Beta pruning and dynamic listing.

- The code is modularized into three main classes and an UI-class:
    - AI-class, which includes everything related to the AI-the game uses mainly minimax and evaluation functions.  
    - Board-class, defines the board used in the game, and simulations during minimax-algorithm.
    - Logic-class, which handles the 'logic' for the actions on the board (movement), and actions regarding different situations (win/draw).
    - The UI-class handles the game-loop which operates the game and turns and manages the dynamic listing of possible moves on the actual game board.

- Python lists are used to create the 2D-array representation of the board, and to store information regarding made and potential moves for the AI.
- ~~If iterative deepening is to be implemented, Python dictionaries will also be utilized for generating best possible move for each situation~~. Not implemented, dynamic listing used instead (Python lists).

### Achieved Time and Space Complexity

- The project achieves time complexity with Minimax with Alpha-Beta Pruning which is O(b^(d/2)) under optimal conditions, (where "b" is the branching factor and "d" is the depth of the tree). Move pruning also reduces the branching factor significantly.

- Space complexity is heavily dependent on the size of the potential moves considered at each stage of the algorithm and the depth used in minimax-algorithm and can be quite significant.
  
### Current State and Improvement suggestions

- The state of the game as of 02.03.2024 is as follows:

    - The AI plays as it should, however one known problem still exist:

    - TODO: Fix AI 'giving up' - make it return the best possible move regardless of game state.

    - TODO: ~~Fix AI playing itself into a 'trap'. At the moment it plays a 4-line even if both sides are blocked, and 5-line is impossible to achieve~~. Fixed as of 02.03.2024

    - TODO: ~~Draw situation is not implemented yet (this is a complete oversight by me unfortunately)~~. Fixed as of 21.02.2024.
 
- Improvement suggestions:
  - Add tasks
  - Add both sides as playable (AI is always X at the moment)
  - Fix AI giving up
  - Add option to replay directly from command line
  
### Used sources

- (https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- (https://en.wikipedia.org/wiki/Minimax)
- (https://en.wikipedia.org/wiki/Gomoku)
- (https://medium.com/codex/play-tic-tac-toe-with-artificial-intelligence-python-bf6725ed44f9)

- Minimax algorithm for Tic-Tac-Toe from Youtube channel The Coding Challenge (https://www.youtube.com/watch?v=trKjYdBASyQ)

- Algorithms Explained – minimax and alpha-beta pruning from Youtube channel Sebastian Lague
(https://www.youtube.com/watch?v=l-hh51ncgDI)

- (https://www3.ntu.edu.sg/home/ehchua/programming/java/JavaGame_TicTacToe_AI.html)
