# HIT137_Assignment2
A repository for our group assignment 2 for the HIT137 class.

## Deadline: 13/09/2024, 22:59

## Table of Contents
- [Setting Up the Environment](#setting-up-the-environment)
    - [Virtual Environment](#virtual-environment)
    - [Installing Requirements](#installing-requirements)
    - [Updating Requirements](#updating-requirements)
- [Project Management on GitHub](#project-management-on-github)



## Setting up the environment

### Virtual Environment
1. Create a virtual environment
    ```bash
    python -m venv .venv
    ```
2. Activate the virtual environment
    - On Windows:
      ```bash
      Set-ExecutionPolicy Unrestricted -Scope Process
      .\.venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```
   *Note: If your IDE automatically uses the virtual environment, you may not need to activate it manually. However, if you are using a terminal outside of your IDE, you will need to activate the virtual environment each time you open a new terminal session.*

    

### Installing Requirements
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Updating Requirements

If new pip packages are required for the assignment, please install the package and update the `requirements.txt` file using the following command:
```bash
pip freeze > requirements.txt
```