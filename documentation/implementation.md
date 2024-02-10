# Implementation Report

- ChatGPT 4 was utilized for information retrieval during this project

### General Structure

- A terminal operated Gomoku game played on a 20x20 game board. AI-opponent in the game utilizes Minimax that is optimized with Alpha-Beta pruning and other optimization techniques include Move Pruning optimization at the moment (10.02.2024). Other optimization techniques will be included later.

- The code is modularized into three main classes:
    - AI-class, which includes everything related to the AI-the game uses mainly minimax.  
    - Board-class, defines the board used in the game, and simulations during minimax-algorithm.
    - Logic-class, which handles the 'logic' for the actions on the board (movement), and actions regarding different situations (win/draw).
    - The UI-class handles the game-loop which operates the game.

- More information will be provided as the project advances

### Achieved Time and Space Complexity

- Will be informed at the end of the project.

### Current State and Improvement suggestions

- The state of the game as of 10.02.2024 is as follows:
    - The AI can play relatively well, however is not thorougly tested so potential problems may arise.
    - Draw situation is not implemented yet (this is a complete oversight by me unfortunately).

- Other improvement suggestions will be added at the end of the project.

### Used sources

- Will be informed at the end of the project.
