#!/usr/bin/env python3

from cmath import pi
import math

def area_of_triangle(a,b):
    a = float(a)
    b= float(b)
    print("The area is {:.6f}".format(a*b/2))

def area_of_rectangle(a,b):
    a = float(a)
    b= float(b)
    print("The area is {:.6f}".format(a*b))

def area_of_circle(a):
    a = float(a)
    print("The area is {:.6f}".format(pi*a**2))




def main():
    # enter you solution here

    shape = input("Choose a shape (triangle, rectangle, circle):")
    while(shape):

        if shape == "triangle":
            base = input("Give base of the triangle: ")
            height = input("Give height of the triangle: ")
            area_of_triangle(base, height)
        elif shape == "rectangle":
            width = input("Give width of the rectangle: ")
            height = input("Give height of the rectangle: ")
            area_of_rectangle(width, height)
        elif shape == "circle":
            radius = input("Give radius of the circle: ")
            area_of_circle(radius)
        else:
            print("Unknown shape!")
        shape = input("Choose a shape (triangle, rectangle, circle):")
        


if __name__ == "__main__":
    main()
