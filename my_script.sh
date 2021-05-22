#!/bin/sh

echo `python3 -m pip --version | cut -d ' ' -f 2`
python3 -m venv local_lib
source local_lib/bin/activate
pip install --upgrade pip
#pip install -r requirements.txt
