from math import sqrt
#set the range of x-values 
xmin = -10
xmax = 10

#range of y-values 
ymin = -10
ymax = 10

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl, yscl 
    background(255) #white
    translate(width/2,height/2) #cyan lines
    grid(xscl, yscl)
    graphFunction()
    
def grid(xscl, yscl):    
    strokeWeight(1) 
    stroke(0,255,255)
    for i in range(xmin,xmax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    
    #creating x-axis and y-axis lines
    stroke(0) #black
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)

def f(x):
    return 2*x**2 + 7*x - 15

def graphFunction():
    x=xmin
    while x<=xmax:
        stroke(255,0,0)
        fill(0,0,255)
        line(x*xscl, f(x)*yscl, (x+0.1)*xscl, f(x+0.1)*yscl)
        x+=0.1
        
def quad(a, b, c):
    return (-b+(sqrt(b**2 - 4*a*c)))/(2*a), (-b-(sqrt(b**2 - 4*a*c)))/(2*a)

print(quad(2,7,-15))
