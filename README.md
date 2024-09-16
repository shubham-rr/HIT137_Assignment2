# HIT137_Assignment2
A repository for our group assignment 2 for the HIT137 class.

## Deadline: 18/09/2024, 22:59 (extended by lecturer)

## Table of Contents
- [Issue with scispacy installation](#issue-with-scispacy-installation)
- [Setting Up the Environment](#setting-up-the-environment)
    - [Virtual Environment](#virtual-environment)
    - [Installing Requirements](#installing-requirements)
    - [Updating Requirements](#updating-requirements)

## Issue with scispacy installation:
Due to installation problems with the latest version of scispacy, please try to install scipacy==0.5.2 on a virtual environment using python 3.8.9 instead.
This is a known error due to nmslib package. You can read more about it here:
https://github.com/allenai/scispacy?tab=readme-ov-file#installation-note-nmslib

## Setting up the environment

### Virtual Environment
1. Create a virtual environment
    ```bash
    python -m venv .venv
    ```
    #### Specifying the version of python
    To address the issues of scispacy installation, please install [python 3.8.9](https://www.python.org/downloads/release/python-389/)
    ***Please do not click add to PATH when installing.***
    It is recommended that you only have one version of python in your PATH variables.
    
    To set up a venv with python 3.8.9:
    ```bash
    C:\Users\replace with your username\AppData\Local\Programs\Python\Python38\python.exe -m venv .venv
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

## Additional information
A "files/" directory should be created within the local repository. This directory will be ignored by git and be used for storing and accessing the original files provided by the lecturer. We ignore this directory because the file sizes are too large to upload on github.