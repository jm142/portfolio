tmux kill-server
cd portfolio
git fetch && git reset origin/main --hard
dnf install tmux
tmux new
python3.8 -m venv python3.8-virtualenv
source python3.8-virtualenv/bin/activate
pip3 install -r requirements.txt
flask run --host=0.0.0.0
