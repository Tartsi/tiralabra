# Implementation Report

- ChatGPT 4 was utilized for information retrieval during this project

### General Structure

- A terminal operated Gomoku game played on a 20x20 game board. AI-opponent in the game utilizes Minimax that is optimized with Alpha-Beta pruning and other optimization techniques include Move Pruning optimization at the moment (10.02.2024). Other optimization techniques will be included later.

- The code is modularized into three main classes and an UI-class:
    - AI-class, which includes everything related to the AI-the game uses mainly minimax.  
    - Board-class, defines the board used in the game, and simulations during minimax-algorithm.
    - Logic-class, which handles the 'logic' for the actions on the board (movement), and actions regarding different situations (win/draw).
    - The UI-class handles the game-loop which operates the game and turns.

- Python lists are used to create the 2D-array representation of the board, and to store information regarding made and potential moves for the AI.
- If iterative deepening is to be implemented, Python dictionaries will also be utilized for generating best possible move for each situation.
- More information will be provided as the project advances

### Achieved Time and Space Complexity

- Will be informed at the end of the project.

### Current State and Improvement suggestions

- The state of the game as of 24.02.2024 is as follows:
    - The AI can play extremely well, however some problems still exist which I already have identified and am working on fixing:
    TODO: Fix AI 'giving up' - make it return the best possible move regardless of game state.
    TODO: Fix AI playing itself into a 'trap'. At the moment it plays a 4-line even if both sides are blocked, and 5-line is impossible to achieve.
    - ~~Draw situation is not implemented yet (this is a complete oversight by me unfortunately)~~. Fixed as of 21.02.2024.

- Other improvement suggestions will be added at the end of the project.

### Used sources

- Will be informed at the end of the project.
