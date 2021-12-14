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
