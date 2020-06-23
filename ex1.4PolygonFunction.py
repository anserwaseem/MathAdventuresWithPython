# Write a function that takes an integer as an arguement and makes the turtle draw a polygon with that integer's umber of sides.

from turtle import *
shape('turtle')

def createPolygon(sideLength=5):
    for i in range(sideLength):
        fd(50)
        rt(360/sideLength)

createPolygon(10)