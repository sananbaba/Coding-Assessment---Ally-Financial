# Sample API Test Using Pytest and SwaggerUI

## System Requirements

python 3.x.x


## Setup

* Install Visual Studio Code (or any editor)

https://code.visualstudio.com/download


* Install Python 3.x.x (latest)

https://www.python.org/downloads/

* Create a project in vscode, open the terminal

```bash
git clone https://github.com/automationExamples/pytest-api-example.git
pip install requests pytest pyhamcrest jsonschema pytest-html flask_restx flask
```

### Recommended vscode extensions

Python, Pylance, autopep8


## Instructions
* You'll need to open two terminal instances, one for the local server, one to run pytest
```bash
python app.py
```
* Once it is running, you can access the SwaggerUI in a browser via http://localhost:5000
* To run the test, use the following command. When the tests complete, a 'report.html' is generated
```bash
pytest -v --html=report.html
```
* It is not expected that you complete every task, however, please give your best effort 
* You will be scored based on your ability to complete the following tasks:

- [ ] Install and setup this repository on your personal computer
- [ ] Complete the automation tasks listed below

### Tasks
- [ ] Extend and fix the 3 tests from [test_pet.py](test_pet.py#1). There are TODO instructions for each test listed in the file
- [ ] Create the PATCH test for [test_store.py](test_store.py#1). There are TODO instructions for test along with optional tasks
- [ ] Take note of any bugs you may have found