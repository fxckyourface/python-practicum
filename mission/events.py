import random

EVENTS = [
    ("Микрометеорит пробил обшивку", -15, 0.4),
    ("Солнечная вспышка: радиация", -10, 0.2),
    ("Удачная коррекция курса", 5, 0.2),
    ("Найдены запасы предыдущей миссии", 20, 0.1),
    ("Отказ системы охлаждения", -25, 0.1)
]

def random_event(seed=None):
    event = random.Random(seed).choices(EVENTS, weights=[e[2] for e in EVENTS], k=1)[0]
    return event[:2]
