import mymodule
from mymodule import circle_area
from mymodule import circle_len as perimeter
import mymodule as mm

print(mymodule.circle_area(2))
print(circle_area(3))
print(perimeter(2))
print(mm.circle_len(3))
print(dir(mymodule))
print(mymodule.__name__)
print(mymodule.__file__)
