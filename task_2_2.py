import random
import math

random.seed(42)
deck = [rank + suit for suit in "♠♥♦♣" for rank in "6789TJQKA"]
print("Рука:", random.sample(deck, 5))
print("Карта дня:", random.choice(deck))
print("Лут:", random.choices(["Обычный", "Редкий", "Легендарный"], weights=[70, 25, 5], k=20))
random.shuffle(deck)
print(deck[:6])
for i in range(3):
    print(f"Игрок {i + 1}:", deck[i * 5:(i + 1) * 5])
print("Лотерея:", sorted(random.sample(range(1, 46), 6)))
print("Вероятность:", 1 / math.comb(45, 6))
