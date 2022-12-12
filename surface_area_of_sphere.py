#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Dec 1, 2022
# This program ask the user to enter the radius of a sphere then tells them the surface area

import math

def calc_surface_ara(radius):


#calculate the surface area
    surface_area = 4*math.pi*(radius*radius)
    surface_area=round(surface_area,2)
    return surface_area

def main():
    #ask user for radius and display surface area
    try:
        surface_area  =""
        radius = float(input("Enter the radius of a sphere: "))
        surface_area = calc_surface_ara(radius)
        print("The surface area is {}" .format(surface_area))
    except:
        print("this is not a number")

if __name__ == "__main__":
    main()