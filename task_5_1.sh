set -eu
cd "$(dirname "$0")"
which python3
python3 -m venv .venv/task_5_1
ls .venv/task_5_1
ls .venv/task_5_1/bin
. .venv/task_5_1/bin/activate
printf '%s\n' "$VIRTUAL_ENV"
which python
python -V
python -m pip list
python -m pip install six
python -m pip list
python -c 'import sys; print(sys.prefix); print(sys.base_prefix); print(sys.prefix != sys.base_prefix)'
deactivate
which python3
