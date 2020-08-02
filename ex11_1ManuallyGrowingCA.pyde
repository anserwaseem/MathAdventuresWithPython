# Using the keyPressed() function (for reference, see Chapter 10) to manually grow the CA.

GRID_H=60 #grid height
GRID_W=60 #grid width
SZ=18 #size of cell

def createCellList():
        '''Creates a big list of OFF cells with
        one ON Cell in the center'''
        newList=[]#empty list for cells
        #populate the initial cell list
        for j in range(GRID_H):
            newList.append([]) #add empty row
            for i in range(GRID_W):
                newList [j].append(Cell(i,j,0)) #add off Cells or zeroes
        #center cell is set to on
        newList [GRID_H//2][GRID_W//2].state = 1
        return newList

class Cell:
    def __init__(self,c,r,state=0): #initially, cell's state is OFF
        self.c = c
        self.r = r
        self.state = state

    def display(self):
        if self.state == 1:
            fill(0) #black
        else:
            fill(255) #white
        rect(SZ*self.r,SZ*self.c,SZ,SZ)

    def checkNeighbors(self):
        if self.state == 1: 
            return 1 #on Cells stay on
        
        neighbs = 0 #check the neighbors
        # check neighbors on left, right, down, up of the current cell
        for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            try:
                if cellList[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue        
        if neighbs in [1,4]:
            return 1
        else:
            return 0

def setup():
    global SZ,cellList
    size(600,600)
    noStroke()
    SZ=width // GRID_W
    cellList = createCellList()

def draw():
    global generation,cellList
    for row in cellList:
        for cell in row:
            cell.display()

def update(cellList):
    newList = []
    for r,row in enumerate(cellList):
        newList.append([])
        for c,cell in enumerate(row):
            newList[r].append(Cell(c,r,cell.checkNeighbors()))
    return newList[::]

#as the mouse clicks, update the cellList
def mouseClicked():
    global cellList
    cellList = update(cellList)
