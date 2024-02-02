# Test report

02.02.2024

### Unit testing

- Unit testing is done by utilizing the unittest-framework. At the moment it encompasses all of the modules inside the services-folder (ai.py, board.py and logic.py). The tests encompass both correct and incorrect inputs, and the goal is to achieve 100% test coverage.
- As of 02.02.2024, all of the methods inside these modules are tested for, expect for the minimax-algorithm itself, which is located in ai.py-module.
- The total number of tests as of 02.02.2024 is 32.

![Test Coverage](/documentation/assets/coverage_report_02_02_2024.png)

### UI-testing

- Done with predetermined inputs.
- UI-testing is quite tricky at the moment because the minimax-algorithm is still under works.
- The UI-itself is also not completely functional, as it cannot handle wrong inputs from the user (or possibly from AI for that matter, however that remains to be tested).

### Other testing (Especially related to Minimax-algorithm)

- Other more complex tests will be implemented later.
