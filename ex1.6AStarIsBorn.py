# Write a star function that will draw a five-pointed star. Next, write a function that will raw a spiral of stars.

from turtle import *
shape('turtle')
speed(0)

def createStar(sideLength=100):
    for i in range(5):
        fd(sideLength)
        rt(180-(180/5))

def starSpiral():
    for j in range(60):
        createStar(j*5)
        right(5)
    
starSpiral()