set -eu
cd "$(dirname "$0")"
project_dir="$PWD"
python3 -m venv .venv/task_4_3
. .venv/task_4_3/bin/activate
python -m pip install ./textkit
python -m pip show -f textkit-demo
cd /tmp
python -c 'from textkit import word_count, char_stats; t="Модули и пакеты в Python"; print(word_count(t)); print(char_stats(t))'
textkit-info
cd "$project_dir"
python -m pip install -e ./textkit
python -c 'import textkit; print(textkit.__file__)'
python -c 'from pathlib import Path; p=Path("textkit/src/textkit/__init__.py"); p.write_text(p.read_text().replace("0.1.0", "0.1.1"))'
python -c 'import textkit; print(textkit.__version__); assert textkit.__version__ == "0.1.1"'
python -c 'from pathlib import Path; p=Path("textkit/src/textkit/__init__.py"); p.write_text(p.read_text().replace("0.1.1", "0.1.0"))'
deactivate
