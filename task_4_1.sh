set -eu
cd "$(dirname "$0")"
python3 -m venv .venv/task_4_1
. .venv/task_4_1/bin/activate
pip -V
python -m pip -V
python -m pip install six
python -m pip show six
python -m pip show -f six
python -m pip list
python -m pip list --outdated
python -c 'import six; print(six.__version__); print(six.__file__)'
python -m pip install --upgrade six
python -m pip uninstall -y six
python -c 'import importlib.util; print(importlib.util.find_spec("six")); assert importlib.util.find_spec("six") is None'
deactivate
