import math

for name in ["pi", "e", "tau", "inf", "nan"]:
    print(name, getattr(math, name))
for func in [math.floor, math.ceil, math.trunc, round]:
    print(func.__name__, func(7.6))
print(round(2.5), round(3.5))
print("При равном расстоянии round выбирает чётное целое")
for name, value in {
    "sqrt(144)": math.sqrt(144), "pow(2,10)": math.pow(2, 10),
    "2**10": 2**10, "exp(1)": math.exp(1), "log(e)": math.log(math.e),
    "log(1024,2)": math.log(1024, 2), "log10(1000)": math.log10(1000),
    "log2(1024)": math.log2(1024), "factorial(10)": math.factorial(10),
    "gcd(48,180)": math.gcd(48, 180), "lcm(4,6)": math.lcm(4, 6),
    "comb(10,3)": math.comb(10, 3), "perm(10,3)": math.perm(10, 3),
    "prod": math.prod([1, 2, 3, 4]), "isqrt(50)": math.isqrt(50)
}.items():
    print(name, value)
print(0.1 + 0.2 == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))
print(sum([0.1] * 10), math.fsum([0.1] * 10))
