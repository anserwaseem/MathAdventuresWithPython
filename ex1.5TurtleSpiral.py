# Write a function to draw 60 squares turning 5 degrees right after each square d making each successive square bigger. Start at length 5 and increment 5 units each square. 

from turtle import *
shape('turtle')
speed(0)

def cTurtleSpiral(length=5):
    for j in range(4):            
        forward(length)
        right(90)

for j in range(60): 
    cTurtleSpiral(j*5+5)
    right(5)