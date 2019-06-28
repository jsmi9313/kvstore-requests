set -e
pyenv local 3.6.0
python -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

