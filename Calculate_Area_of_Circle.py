#Programer: Sachorra Douglas
#Assignment: Use epython to calculate the area of a circle
#Date: 11/13/2024

import math

def calculate_area_of_circle():
    #Prompt the user to enter the radius of the circle
    radius = int(input("Enter the radius of the circle: "))

    #Calculate the area using the formula: Area = π * r^2
    area = math.pi * (radius ** 2)

    #Print the result
    print(f"The area of the circle with radius {radius} is: {area: .2f}")

#Run the program
calculate_area_of_circle()
