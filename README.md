#QA Automated testing framework in Python

## Description
This project was created while studying QA automated testing. It's purpose to learn how to create automate testing framework with API, UI and database tests.
Technologies used:
- pytest
- sqlite3
- selenium
## Project structure
+---config
+---modules
|   +---api
|   |   \---clients
|   +---common
|   \---ui
|       \---page_objects
\---tests
    +---api
    +---database
    \---ui

## Runing tests
All tests are divided by markers that can be found in pytest.ini file.
List of markers:
 - 
To run test with specisific marker use command
pytest -m api

