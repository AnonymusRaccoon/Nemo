#! /usr/bin/sh

. venv/bin/activate
pip install -U discord.py

export NEMO_TOKEN='INSERT YOUR TOKEN HERE'
python3 nemo.py