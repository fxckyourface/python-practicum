import sys
import math
import random

print("Версия Python:", sys.version)
print("Интерпретатор:", sys.executable)
print("Число путей:", len(sys.path))
for path in sys.path[:4]:
    print("   ", path)
print("pi:", math.pi)
print("Случайное число:", random.random())
print("Загружено модулей:", len(sys.modules))
print(sorted(sys.modules)[:5])
print("Публичных имён math:", len([name for name in dir(math) if not name.startswith("_")]))
