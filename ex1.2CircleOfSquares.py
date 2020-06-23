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