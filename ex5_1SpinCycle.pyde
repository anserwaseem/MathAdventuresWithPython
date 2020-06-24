# Create a circle of equilateral triangles in a Processing sketch, and rotate them using the rotate() function.

def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB)
    
t=0

def draw():
    global t
    background(255)
    translate(width/2, height/2)
    rotate(radians(t))
    for i in range(90):
        pushMatrix() #save this orientation
        translate(200,0)
        rotate(radians(t))
        tri(30)
        popMatrix() #return to the saved orientation
        rotate(radians(360/12))
    t+=0.5
            
def tri(length):
    #Draws an equilateral triangle around centre of triangle 
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
