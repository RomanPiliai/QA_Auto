#QA Automated testing framework in Python

## Description
This project was created while studying QA automated testing. The purpose of this project is to learn how to create an automated testing framework with API, UI, and database tests.
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

## Running tests
All tests are divided by markers found in the pytest.ini file.
List of markers:
 - 
To run a test with specific marker use the command
pytest -m api

