#!/bin/bash -ex

# virtual environment
python3 -m venv venv
. venv/bin/activate

# start flask server
env FLASK_APP=$1 env FLASK_ENV=development flask run
