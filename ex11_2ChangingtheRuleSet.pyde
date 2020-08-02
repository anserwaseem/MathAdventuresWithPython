''' Rule 30 was introduced by Stephan Wolfram in 1983.
    Creating Rule 90 design using Cellular Automation.
    Change the value of w, rows, and cols to explore the design.
'''

w = 5 #width of each cell
rows = 200
cols = 200
#--snip--
ruleset = [0,1,0,1,1,0,1,0] #rule 90

def setup():
    global cells
    size(600,600)
    noStroke()
    #first row:
    cells = []
    for r in range(rows):
        cells.append([])
        for c in range(cols):
            cells[r].append(0)
        cells[0][cols//2] = 1
    cells = generate()

def draw():
    background(255) #white
    #draw the CA
    for i, cell in enumerate(cells): #rows
        for j, v in enumerate(cell): #columns
            if v == 1:
                fill(0)
            else:
                fill(255)
            rect(j*w-(cols*w-width)/2,w*i,w,w)

#connverting from binary to decimal
#the indices are in reverse order, so we subtract the total from 7 to get the proper index of the ruleset.
def rules(a,b,c):
       return ruleset[7 - (4*a + 2*b + c)]

def generate():
       for i, row in enumerate(cells): #look at first row
           for j in range(1,len(row)-1):
               left = row[j-1]
               me = row[j]
               right = row[j+1]
               if i < len(cells) - 1:
                    cells[i+1][j] = rules(left,me,right)
       return cells
