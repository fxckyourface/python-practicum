set -eu
cd "$(dirname "$0")"
python3 -m venv .venv/conflict
.venv/conflict/bin/python -m pip install packaging==24.0
.venv/conflict/bin/python -c 'import packaging; print(packaging.__version__)'
.venv/conflict/bin/python -m pip install packaging==21.0
.venv/conflict/bin/python -c 'import packaging; print(packaging.__version__)'
python3 -m venv .venv/project_a
python3 -m venv .venv/project_b
.venv/project_a/bin/python -m pip install packaging==21.0
.venv/project_b/bin/python -m pip install packaging==24.0
. .venv/project_a/bin/activate
python -c 'import packaging; print("A:", packaging.__version__)'
deactivate
. .venv/project_b/bin/activate
python -c 'import packaging; print("B:", packaging.__version__)'
deactivate
