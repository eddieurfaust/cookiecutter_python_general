@echo off
setlocal

:: Create and activate virtual environment
python -m venv .venv
call .venv\Scripts\activate

:: Install pylint and black
pip install pylint black

:: Download pylintrc from Google Style Guide
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/google/styleguide/gh-pages/pylintrc' -OutFile '.\.pylintrc'"

:: Initialize a Git repository and make an initial commit
git init .
git add .
git commit -m "Initial commit"

endlocal
