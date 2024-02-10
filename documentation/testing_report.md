# Test report

10.02.2024

### Unit testing

- Unit testing is done by utilizing the unittest-framework. At the moment it encompasses all of the modules inside the services-folder (ai.py, board.py and logic.py). The tests encompass both correct and incorrect inputs, and the goal is to achieve 100% test coverage.
- As of 10.02.2024, all of the methods inside these modules are tested for, expect for the minimax-algorithm itself, which is located in ai.py-module.
- The total number of tests as of 10.02.2024 is 36.

![Tests](/documentation/assets/Tests_10_02_2024.png)
![Test Coverage](/documentation/assets/Coverage_10_02_2024.png)

### UI-testing

- Done with predetermined inputs.
- AI consistently looks for a win, and builds good lines. It also blocks the player relatively effectively.
- More UI testing to be done later.

### Other testing (Especially related to Minimax-algorithm)

- Other more complex tests will be implemented later.
