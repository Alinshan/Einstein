if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Alinshan/Einstein.git /Einstein
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Einstein
fi
cd /Ajax
pip3 install -U -r requirements.txt
echo "Starting Einstein....🔥"
python3 bot.py
