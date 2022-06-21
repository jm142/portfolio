#!/bin/bash
tmux kill-server
cd portfolio
git fetch && git reset origin/main --hard
dnf install tmux
tmux -d new -s $1 "python3.8 -m venv python3.8-virtualenv; source python3.8-virtualenv/bin/activate; pip3 install -r requirements.txt; flask run --host=0.0.0.0"
