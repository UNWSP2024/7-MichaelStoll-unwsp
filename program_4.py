#title:coordinates
#author: michael stoll
#date: 3/6/2025
import math

def coordinates():
    coordinate_set1 = (x1,y1,z1)
    coordinate_set2 = (x2,y2,z2)
    print(coordinate_set1, coordinate_set2)

x1 = int(input('Enter first x coordinate:'))
y1 = int(input('Enter first y coordinate:'))
z1 = int(input('Enter first z coordinate:'))
x2 = int(input('Enter second x coordinate:'))
y2 = int(input('Enter second y coordinate:'))
z2 = int(input('Enter second z coordinate:'))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z1 - z2)**2)
coordinates()
print(f'The distance between the two coordinates is {distance} units')