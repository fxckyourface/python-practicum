set -eu
cd "$(dirname "$0")"
python3 -m venv .venv/task_4_2
. .venv/task_4_2/bin/activate
python -m pip install -r requirements.txt
python -m pip freeze
python -m pip check
python -m pip install --upgrade packaging
python -m pip freeze > requirements.lock.txt
deactivate
