import math

def area_circum_circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, b = area_circum_circle(3)


print("The area of the circle is:", round(a, 2))
print("The circumference of the circle is:", round(b, 2))