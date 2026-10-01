import geometry
from geometry import circle_area, triangle_area
from geometry.solid import sphere_volume, cube_volume, hemisphere_area

print(geometry.circle_area(2))
print(circle_area(3), triangle_area(4, 5))
print(sphere_volume(2), cube_volume(3), hemisphere_area(2))
print(geometry.__file__)
