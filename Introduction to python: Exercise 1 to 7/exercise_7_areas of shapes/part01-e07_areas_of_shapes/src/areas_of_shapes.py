#!/usr/bin/env python3

# Exercise 7 (areas of shapes)
# Create a program that can compute the areas of three shapes,
# triangles, rectangles and circles, when their dimensions are given.
#
# An endless loop should ask for which shape you want the area be
# calculated. An empty string as input will exit the loop. If the user
# gives a string that is none of the given shapes, the message “unknown
# shape!” should be printed. Then it will ask for dimensions for that
# particular shape. When all the necessary dimensions are given, it
# prints the area, and starts the loop all over again. Use format
# specifier f for the area.
#
# What happens if you give incorrect dimensions, like giving string “aa”
# as radius? You don’t have to check for errors in the input.
#
# Example interaction:
#
# Choose a shape (triangle, rectangle, circle): triangle
# Give base of the triangle: 20
# Give height of the triangle: 5
# The area is 50.000000
# Choose a shape (triangle, rectangle, circle): rectangel
# Unknown shape!
# Choose a shape (triangle, rectangle, circle): rectangle
# Give width of the rectangle: 20
# Give height of the rectangle: 4
# The area is 80.000000
# Choose a shape (triangle, rectangle, circle): circle
# Give radius of the circle: 10
# The area is 314.159265
# Choose a shape (triangle, rectangle, circle):



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
