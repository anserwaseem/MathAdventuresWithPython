#Julia "laces" defined from a function. Julia set consists of values such that an arbitrarily small perturbation can cause drastic changes in the sequence of iterated function values. Its behavior is "chaotic".

from math import sqrt

#range of x-values
xmin = -2
xmax = 2

#range of y-values
ymin = -2
ymax = 2

#calculate the range of x and y
rangex = xmax - xmin 
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)#Hue, Saturation, Brightness
    noStroke()
    xscl=width/float(rangex)
    yscl=height/float(rangey)
    
def draw():
    #origin in center: 
    translate(width/2,height/2)
    #go over all x's and y's on the grid 
    x = xmin #initialize to xmin value
    while x < xmax: #run the loop until xmax
        y = ymin #initialize to ymin value
        while y < ymax: #run the loop until ymax
            z = [x,y]
            c = [0.285,0.01]
            #put it into the julia program 
            col = julia(z,c,100)
            #if julia returns 100
            if col == 100:
                fill(0)
            else:
                #map the color from 0 to 100
                #to 0 to 255
                #coll = map(col,0,100,0,300)
                fill(3*col,255,255)
            rect(x*xscl,y*yscl,1,1)
            y += 0.01 
        x += 0.01
                
def julia(z, c, num):
    '''runs the process num times and returns the diverge count'''
    count=0;
    z1=z
    while count <= num:
        if magnitude(z1) > 2.0: #return count when magnitude exceeds 2.0
            return count
        z1=cAdd(cMult(z1,z1),c) #square the complex number z1, then add it in constant complex number c
        count+=1
    return num #return the diverge count

def cMult(u,v):
    '''Multiply the given two complex numbers and return their result.'''
    return [u[0]*v[0]-u[1]*v[1], u[0]*v[1]+u[1]*v[0]]

def cAdd(u,v):
    '''Add the given two complex numbers and return their result.'''
    return [u[0]+v[0], u[1]+v[1]]

def magnitude(u):
    '''Returns magnitude of a given complex number.'''
    return sqrt(u[0]**2 + u[1]**2)
