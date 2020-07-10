from random import choice

WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)

class Sheep:
    def __init__(self,x,y,col):
        self.x = x #x-position
        self.y = y #y-position
        self.sz = 10 #size
        self.energy = 30 #energy level
        self.eaten = False
        self.col = col
        self.age = 0 #age of sheep

    def update(self):
        #make sheep walk randomly
        move = 5 #the maximum it can move in any direction
        self.energy -= 1 #walking costs energy
        self.age += 0.1 #sheep loses a small part of its age as it walks
        if self.energy <= 0 or self.age >= 10: #remove a Sheep if energy is finished or its time is finished.
            sheepList.remove(self)
        if self.energy >= 50:
            self.energy -= 30 #giving birth takes energy
            #add another sheep to the list
            sheepList.append(Sheep(self.x,self.y,self.col))
        self.x += random(-move, move)
        self.y += random(-move, move)
        #"wrap" the world Asteroids-style
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        #find the patch of grass you're on in the grassList:
        xscl = int(self.x / patchSize)
        yscl = int(self.y / patchSize)
        grass = grassList[xscl * rows_of_grass + yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        fill(self.col) #its own color
        ellipse(self.x,self.y,self.sz,self.sz)

class Grass:
    def __init__(self,x,y,sz):
        self.x = x #x-position
        self.y = y #y-position
        self.energy = 10 #energy from eating this patch
        self.eaten = False #hasn't been eaten yet
        self.sz = sz

    def update(self):
        if self.eaten:
            if random(100) < 5:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)
    
sheepList = [] #list to store sheep
grassList = [] #list to store grass“def setup():
patchSize = 10 #size of each patch of grass
colorList = [WHITE,RED,YELLOW,PURPLE]

def setup():
    global patchSize, rows_of_grass
    size(600,600)
    rows_of_grass = height/patchSize
    noStroke()
    #create the sheep
    for i in range(20):
        sheepList.append(Sheep(random(width),random(height),choice(colorList)))
    #create the grass:
    for x in range(0,width,patchSize):
        for y in range(0,height,patchSize):
            grassList.append(Grass(x,y,patchSize))
            
def draw():
    background(255)
    #update the grass first
    for grass in grassList:
        grass.update()
    #then the sheep
    for sheep in sheepList:
        sheep.update()
