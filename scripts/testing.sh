#!/bin/bash

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

py -m pytest --cov=. --cov-report html