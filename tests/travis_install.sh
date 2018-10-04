#!/bin/bash
virtualenv --no-site-packages .venv
source .venv/bin/activate
pip install ansible==2.5.0
pip install -r install.txt
