import argparse
from .stats import word_count, char_stats

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="?", default="Модули и пакеты в Python")
    args = parser.parse_args()
    print("Слов:", word_count(args.text), "| Статистика:", char_stats(args.text))

if __name__ == "__main__":
    main()
