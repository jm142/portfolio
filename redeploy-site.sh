#!/bin/bash
tmux kill-server
git fetch && git reset origin/main --hard
source python3.8-virtualenv/bin/activate
python3.8 -m pip install -r requirements.txt
tmux new-session -d -s Flask
tmux send-keys 'source python3.8-virtualenv/bin/activate' C-m
tmux send-keys 'python3.8 -m flask run --host=0.0.0.0' C-m
tmux detach -s Flask
