# FakeRestAPI.Web Tests

In this repository can be found the tests for the [FakeRestAPI.Web](https://fakerestapi.azurewebsites.net/swagger/ui/index#/) API.

## Getting Started

### Overview

This project runs on [python3](https://www.python.org/download/releases/3.0/).

### Project Setup

Before installing, download and install Python3. For Linux or Mac [brew](https://brew.sh/) can be used to install python3.
    $ brew install python3

Pip3 should be available upon the installation of python3, if not it needs to be installed as well.

To check if python3 and pip3 are installed please run:
    $ pyhton3 --version
    $ pip3 --version

With python3 and pip3 is required to install `requests` and `pytest` dependencies:
    $ pip3 install -U requests
    $ pip3 install -U pytest

### Run tests

The tests can be executed by running the `run-tests` script in the commamd line under the project folder:
    $ ./run-tests.sh
