'''.......Define a function that accepts radius and returns the area of a circle.......?'''


def Area_of_circle (radius):

    Area = (3.14 * radius **2)

    return Area 

radius = float(input('Radius of the circle:'))

Area = Area_of_circle(radius)

print('Area of the circle: ',Area)