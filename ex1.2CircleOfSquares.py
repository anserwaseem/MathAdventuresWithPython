# Write and run a function that draws 60 squares, turning right 5 degrees after each square. Use a loop!

from turtle import *
shape('turtle')
speed(0)

def createSquares():
    for j in range(4):            
        forward(100)
        right(90)

for j in range(60): 
    createSquares()
    right(5)
