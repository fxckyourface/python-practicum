from math import pi as PI

VERSION = "1.0.0"

def circle_area(r):
    return PI * r ** 2

def circle_len(r):
    return 2 * PI * r

def _helper():
    return VERSION

if __name__ == "__main__":
    print(_helper(), circle_area(2), circle_len(2))
