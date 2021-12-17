# HMC Room Draw Logic and Action
Enforces the logic functions of HMC Room Draw and performs the actions a user can do in HMC Room Draw
## Testing
1. Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Install python 3.10
```bash
brew install python@3.10
```
3. Clone the repository
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
