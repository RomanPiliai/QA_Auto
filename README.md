# QA Automated testing framework in Python

## Description
This project was created while studying QA automated testing. The purpose of this project is to learn how to create an automated testing framework with API, UI, and database tests.
Technologies used:
- pytest
- sqlite3
- selenium
## Project structure
  +---config
 <br/>+---modules
 <br/>|   +---api
 <br/>|   |   \---clients
 <br/>|   +---common
 <br/>|   \---ui
 <br/>|       \---page_objects
 <br/>\---tests
 <br/>    +---api
 <br/>    +---database
 <br/>    \---ui

## Running tests
All tests are divided by markers found in the pytest.ini file.
List of markers:
 - change: Tests that modify name of a user
 - check: Tests that check user name
 - http: Tests that check HTTP Protocol
 -  api: Tests that check api
 -  database: Tests connection to database
 -  ui: Tests UI
   
To run a test with specific marker use the command
```bash
pytest -m [marker name]
```
