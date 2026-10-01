set -eu
cd "$(dirname "$0")"
python3 -m venv .venv/uv_tool
.venv/uv_tool/bin/python -m pip install uv
uv_bin="$PWD/.venv/uv_tool/bin/uv"
"$uv_bin" --version
"$uv_bin" venv --seed .venv/task_6_1
"$uv_bin" pip install requests --python .venv/task_6_1/bin/python
"$uv_bin" pip list --python .venv/task_6_1/bin/python
"$uv_bin" pip tree --python .venv/task_6_1/bin/python
. .venv/task_6_1/bin/activate
python -m pip list
deactivate
python3 -m venv .venv/pip_benchmark
"$uv_bin" venv --seed .venv/uv_benchmark
time .venv/pip_benchmark/bin/python -m pip install --no-cache-dir requests
time "$uv_bin" pip install --no-cache requests --python .venv/uv_benchmark/bin/python
