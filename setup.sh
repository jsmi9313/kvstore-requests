# Exit on error
set -e

printf -- '--------------------------------\n\tSETUP LOCAL PYENV.\n--------------------------------\n'
pyenv local 3.6.0

printf '\n--------------------------------\n\tLOCAL VENV.\n--------------------------------\n'
python -m venv venv

printf '\n--------------------------------\n\tACTIVATE VENV.\n--------------------------------\n'
. venv/bin/activate

printf '\n--------------------------------\n\tUPGRADE PIP.\n--------------------------------\n'
pip install --upgrade pip

printf '\n--------------------------------\n\tINSTALL REQS.\n--------------------------------\n'
pip install -r requirements.txt

