tmux kill-session -t portfolio
cd portfolio
git fetch && git reset origin/main --hard
python3.8 -m venv python3.8-virtualenv
source python3.8-virtualenv/bin/activate
pip install -r requirements.txt
clear
tmux new -d -s  portfolio
tmux send -t portfolio "flask run --host=0.0.0.0" ENTER
cd
