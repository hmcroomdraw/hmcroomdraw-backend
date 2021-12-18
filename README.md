# hmcroomdraw-backend
The backend of the CS181AA room draw website

## Installation (macOS)
1. Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Install python 3.9
```bash
brew install python@3.9
```
3. Install pipenv
```bash
pip3 install pipenv
```
4. Clone the repository
```bash
git clone https://github.com/hmcroomdraw/hmcroomdraw-backend.git
```
5. Open the cloned directory
```bash
cd hmcroomdraw-backend
```
6. Install the dependencies using pipenv
```bash
pipenv install
```
7. Every time you restart the terminal, you have to enter the virtual environment before you can run the server.
```bash
pipenv shell
```

## Run the tests
```
python -m unittest
```

## Initialize the database
```
python -c "import repository; repository.init_db()"
```

## Run the server
```
python server.py
```
- If you are using Visual Studio Code, you could also go to `Run and Debug` > `Python: Flask` instead of typing this in the terminal.

## Overview of contained files
1. `api.yaml` defines the api endpoints accessible of the server (Shared)
2. `server.py` contains the web-server and endpoint implementations (Santi)
3. `repository.py` contains the part of the code that connects to the database (Santi)
4. `roomdraw_logic.py` contains the pulling and priority definitions (Adi)
5. `schema.sql` contains the database schema (Santi)
6. `initial_minimal.sql` contains a script that creates a minimmal database that demonstrates room draw functionalities (Santi)
