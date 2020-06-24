# Make Roger Antonsen's sketch "90 Rotating Equilateral Triangles" and color each triangle using stroke().

def setup():
    size(1400, 800)
    rectMode(CENTER)
    colorMode(HSB)
    
t=0

def draw():
    global t
    background(0)
    translate(width/2, height/2)
    rotate(radians(t))
    for i in range(90):
        rotate(radians(360/90)) #space the triangles evenly to cover up whole 360 degrees i.e., 4 degree each
        pushMatrix() #save this orientation
        translate(200,0) #go to circumference
        rotate(radians(t+i*360/45)) #spin each triangle with phase-shifting so that Roger Antonsen's sketch can be made
        stroke(255-i*255/90, 255, 255) #hue is varied such that a unique color can be obtained while keeping saturation and brightness constant
        tri(t) # make a triangle of t length
        popMatrix() #return to the saved orientation
    t+=0.5
            
def tri(length):
    #Draws an equilateral triangle around centre of triangle 
    noFill()
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
