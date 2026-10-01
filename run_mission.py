import argparse
import sched
import time
from mission import delta_v, flight_time, fuel_needed, random_event

def build_parser():
    parser = argparse.ArgumentParser(description="Симулятор межпланетной миссии")
    parser.add_argument("--days", type=int, default=5)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--speed", type=float, default=0.2)
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.days < 1 or args.speed < 0 or not __import__("math").isfinite(args.speed):
        parser.error("days должен быть положительным, speed — конечным и неотрицательным")
    resource = 100
    s = sched.scheduler(time.monotonic, time.sleep)
    print("МИССИЯ АРЕС-1: Марс")
    print(f"Характеристическая скорость: {delta_v(45000, 20000):.1f} м/с")
    print(f"Топливо: {fuel_needed(20000, 4000):,.0f} кг")
    hours = flight_time(78340000, 0.003)
    print(f"Время перелёта: {hours:,.0f} ч = {hours / 24:.0f} сут")

    def day_report(day):
        nonlocal resource
        desc, delta = random_event(args.seed + day if args.seed is not None else None)
        resource = max(0, min(100, resource + delta))
        print(f"Сутки {day:2} | {desc:<38} {delta:+3} | ресурс {resource:3}% {'#' * (resource // 5)}")
        if resource == 0:
            for event in list(s.queue):
                s.cancel(event)
            print("Миссия прервана")

    start = time.monotonic()
    for day in range(1, args.days + 1):
        s.enterabs(start + day * args.speed, 1, day_report, (day,))
    s.run()
    print(f"Итоговый ресурс: {resource}%")

if __name__ == "__main__":
    main()
