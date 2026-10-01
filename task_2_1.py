import random
from collections import Counter

random.seed(42)
print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 6))
print(random.randrange(0, 100, 5))
for _ in range(5):
    a, b = random.randint(1, 6), random.randint(1, 6)
    print(a, b, a + b)
counts = Counter(random.randint(1, 6) for _ in range(10000))
for face in range(1, 7):
    percent = counts[face] / 100
    print(f"{face}: {counts[face]:4d} {percent:.2f}% {'#' * round(percent)}; отклонение {percent - 100 / 6:+.2f}%")
