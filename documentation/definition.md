# Project definition

- Programme: Bachelor's in Computer Science

- In this project, I will be using Python and doing the documentation and code in English. When it comes to other languages, I am familiar enough with Java to give feedback on other projects.

- I am going to develop an AI for 20x20 Gomoku-game (aka. Tic-Tac-Toe). The AI should be able to compete against human opponents and against itself. The required optimization for this project is Move Pruning Optimization. We will only consider free squares, with a maximum distance of 2 from the previous moves. A dynamic list is to be kept of these squares, which will be updated as the computations go on. This list will then be passed on as a parameter in the recursive calls of the minimax-algorithm.
- This project is one of the potential topic suggestions on the course page.

### Algorithms and Data Structures and why they were chosen:

- Minimax Algorithm with Alpha-Beta Pruning: This algorithm will serve as the foundation of the AI's decision-making process. It simulates possible moves in the game and their outcomes, aiming to minimize the possible loss in a worst-case scenario.
- Move Pruning Optimization: Required optimization. Limit the AI's consideration to free squares within two squares of previously made moves, maintaining a dynamic list of these potential move positions.
- Python lists [Dynamic Array]: These will be used to dynamically store the game state, list of potential moves, and other necessary data during the AI's computation.
- 2D Array - Game board: The game board will be represented as a 2D array.

### What problem is being solved?

- The primary problem being solved is developing an efficient and competitive AI for playing the game.

### Inputs to the Program and Their Usage:

- Game State: 2D array, indicating the positions of both players' markers on the board.
- Player's Move: The coordinates of the player's move, which the AI will use to update the game state and compute its response.
- The inputs are used to maintain the game state and drive the AI's decision-making process

### Time Complexity:

- Minimax with Alpha-Beta Pruning aims for a time complexity better than the plain minimax-algorithm which is O(b^d) (where "b" is the branching factor and "d" is the depth of the tree). Also the required Move Pruning Optimization is designed to significantly reduce the branching factor "b" in the minimax-algorithm by focusing only on specific moves.

### Space Complexity:

- The use of dynamic arrays and 2D arrays aims for space-efficient storage of the game state and potential moves. The space complexity is heavily dependent on the size of the potential moves considered at each stage of the algorithm.

### Sources:

- (https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- (https://en.wikipedia.org/wiki/Minimax)
- (https://en.wikipedia.org/wiki/Gomoku)
- (https://medium.com/codex/play-tic-tac-toe-with-artificial-intelligence-python-bf6725ed44f9)
