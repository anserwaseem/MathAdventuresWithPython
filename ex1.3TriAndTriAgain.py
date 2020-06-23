# Write a function that draws a triangle with given side length.

from turtle import *
shape('turtle')

def createTriangle(sideLength=100):
    for i in range(3):
        fd(sideLength)
        rt(-120)

createTriangle(50)