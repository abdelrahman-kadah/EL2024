def getCircleArea(radius):
    pi = 3.14
    return pi * radius * radius

radius = float(input("Enter the circle radius:"))
print(f"The area of radius {radius} is {getCircleArea(radius)}")
