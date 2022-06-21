#!/bin/bash
tmux kill-server
cd portfolio
git fetch && git reset origin/main --hard
dnf install tmux
source python3.8-virtualenv/bin/activate
pip3 install -r requirements.txt;
tmux new -ds $1 "flask run --host=0.0.0.0"
