# Test report

08.03.2024

### Unit testing

- Unit testing is done by utilizing the unittest-framework. At the moment it encompasses all of the modules inside the services-folder (ai.py, board.py and logic.py). The tests encompass both correct and incorrect inputs, and the goal is to achieve 100% test coverage (99% ultimately achieved).

- All of the methods inside these modules are tested for, with ai.py having 1 partial in the update_possible_moves - function.

- The total number of tests is 43.

![Test Coverage](/documentation/assets/test_coverage_final.png)
![Test Coverage Report](/documentation/assets/coverage_report_final.png)

### UI-testing

- Done with predetermined inputs.

- AI consistently looks for a win, and builds good lines. It also blocks the player effectively and can see winning plays in advance. In other words, it plays as well as it can given the evaluation functions and the acquired depth in the project.

- TODO: ~~Fix AI 'giving up' if faced with inevitable loss. Make it return best move regardless.~~ Fixed as of 05.03.2024.

- TODO: ~~AI will take a 4:th line in a direction, even if the player has blocked both sides, such as that it is impossible to build a 5-straight line~~. Fixed on 02.03.2024.


### Other testing

- No other specialized testing will be available for this project.
