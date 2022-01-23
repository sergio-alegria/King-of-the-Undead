#! /bin/bash

# Install Python3 and Pip3
sudo apt install python3 -y python3-pip -y > /dev/null 2>&1

# Install requirements for game
pip install -r requirements.txt

# Get Python3 path
python=$(which python3)

# Launch main menu
$python src/launcher.py

