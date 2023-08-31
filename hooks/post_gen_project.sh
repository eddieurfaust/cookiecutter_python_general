#!/bin/bash

# create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install pylint black

# download pylint config
wget -O .pylintrc https://raw.githubusercontent.com/google/styleguide/gh-pages/pylintrc

# initialize git repo
git init .
git add .
git commit -m "Initial commit"
