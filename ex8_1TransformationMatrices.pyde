#change the values of transformation_matrix to [[1,0],[0,-1]] and [[0,-1],[-1,0]] and [[-1,1],[1,1]] to see the changes.
#We draw a simple figure and transform it using matrices. Letter F is used because it has no rotational or reflectional symmetry

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
    #the scale factors for drawing on the grid: 
    xscl= width/rangex
    yscl= -height/rangey
    noFill()
    
def draw():
    global xscl, yscl 
    background(255) #white 
    translate(width/2,height/2) 
    grid(xscl, yscl)
    strokeWeight(2) #thicker line
    stroke(0) #black
    newmatrix = transpose( multmatrix( transformation_matrix, transpose(fmatrix) ) )
    graphPoints(fmatrix)
    stroke(255,0,0) #red resultant matrix
    graphPoints(newmatrix)

'''
in 2D, consider a matrix that rotates a given matrix by a counter-clockwise angle 0 theta in a fixed coordinate system.
Then,
     R(0) = [ [cos0, -sin0],[sin0, cos0] ]
So,
     new_matrix = transformation_matrix * given_matrix
'''    
transformation_matrix = [[-1,1],[1,1]]
fmatrix = [[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],[3,4],[3,5],[0,5]]

def graphPoints(matrix):
    #draw line segments between consecutive points
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl,pt[1]*yscl)
    endShape(CLOSE)
    
def multmatrix(a,b):
    #Returns the product of matrix a and matrix b
    m = len(a) #number of rows in first matrix
    n = len(b[0]) #number of columns in second matrix
    newmatrix = []
    for i in range(m):
        row = []
        #for every column in b
        for j in range(n):
            sum1 = 0
            #for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

def transpose(a):
    '''Transposes matrix a'''
    output = []
    m = len(a)
    n = len(a[0])
    #create an n x m matrix
    for i in range(n):
        output.append([]) 
        for j in range(m):
            #replace a[i][j] with a[j][i]
            output[i].append(a[j][i]) 
    return output

def grid(xscl,yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
