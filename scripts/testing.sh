#!/bin/bash
sudo apt-get update
sudo apt-get install python3.10-venv -y

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 -m pytest --cov=. --cov-report html