# Test report

02.03.2024

### Unit testing

- Unit testing is done by utilizing the unittest-framework. At the moment it encompasses all of the modules inside the services-folder (ai.py, board.py and logic.py). The tests encompass both correct and incorrect inputs, and the goal is to achieve 100% test coverage.

- For the , all of the methods inside these modules are tested for, with minimax-algorithm missing and having 1 partial branch, which I could not solve for some reason.

- The total number of tests is 41.

![Tests](/documentation/assets/coverage_02_03.png)
![Test Coverage](/documentation/assets/coverage_report_02_03.png)

### UI-testing

- Done with predetermined inputs.

- AI consistently looks for a win, and builds good lines. It also blocks the player effectively.

- TODO: Fix AI 'giving up' if faced with inevitable loss. Make it return best move regardless.
- Was not able to fix this due to lack of time, and dynamic listing taking up so much of the progress last week, especially when I had to scrap most of the progress done on Monday and Tuesday.

- TODO: ~~AI will take a 4:th line in a direction, even if the player has blocked both sides, such as that it is impossible to build a 5-straight line~~. Fixed on 02.03.2024.


### Other testing

- No other specialized testing will be available for this project.
