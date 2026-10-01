import sched
import time

s = sched.scheduler(time.time, time.sleep)
start = time.time()

def say(text):
    print(f"{time.time() - start:.2f} с | {text}")

s.enter(1, 1, say, ("Первое событие",))
s.enterabs(start + 2, 1, say, ("Приоритет 1",))
s.enterabs(start + 2, 0, say, ("Приоритет 0",))
s.enter(4, 1, say, ("Четвёртое событие",))
s.enter(5, 1, say, ("Пятое событие",))
s.enterabs(start + 3, 1, say, ("Абсолютное время",))
print("Размер очереди:", len(s.queue))
s.run()
print("Очередь пуста:", s.empty())
