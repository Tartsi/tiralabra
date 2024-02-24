# Test report

24.02.2024

### Unit testing

- Unit testing is done by utilizing the unittest-framework. At the moment it encompasses all of the modules inside the services-folder (ai.py, board.py and logic.py). The tests encompass both correct and incorrect inputs, and the goal is to achieve 100% test coverage.

- As of 24.02.2024, all of the methods inside these modules are tested for, with minimax-algorithm missing and having 1 partial branch.

- The total number of tests as of 24.02.2024 is 39.

![Tests](/documentation/assets/Tests_24_02_2024.png)
![Test Coverage](/documentation/assets/Coverage_24_02_2024.png)

### UI-testing

- Done with predetermined inputs.

- AI consistently looks for a win, and builds good lines agressively. It also blocks the player effectively.

- TODO: Fix AI 'giving up' if faced with inevitable loss. Make it return best move regardless.
- TODO: AI will take a 4:th line in a direction, even if the player has blocked both sides, such as that it is impossible to build a 5-straight line.

### Other testing

- No other specialized testing will be available for this project.
