import math

radius = float(input('Enter radius of circle: '))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('Area = %0.4f.' % (area))
print('Circumference = %0.4f.' % (circumference))