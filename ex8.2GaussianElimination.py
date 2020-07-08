#Solving the system of equations for w, x, y, and z using Gauss-Elimination method.

def gauss(A):
    '''Converts a matrix into the identity
    matrix by Gaussian elimination, with
    the last column containing the solutions
    for the variables'''
    rows = len(A)#rows
    cols = len(A[0])#columns
    for j,rowNo in enumerate(A):
        #diagonal term to be 1 by dividing row by diagonal term
        if rowNo[j] != 0: #diagonal entry can't be zero
            divisor = rowNo[j]
        for i, term in enumerate(rowNo):
            rowNo[i] = term / divisor
        #add the other rows to the additive inverse for every row
        for i in range(rows):
            if i != j: #don't do it to row j
                #calculate the additive inverse
                addinv = -1*A[i][j]
                #for every term in the ith row
                for ind in range(cols):
                    #add the corresponding term in the jth row multiplied by the additive inverse to the term in the ith row
                    A[i][ind] += addinv*A[j][ind]
    return A
#example:
'''
2w- x+5y+ z=-3
3w+2x+2y-6z=-32
 w+3x+3y- z=-47
5w-2z-3y+3z=49
'''
A = [[2,-1,5,1, -3],
     [3,2,2,-6, -32],
     [1,3,3,-1, -47],
     [5,-2,-3,3, 49]]
print(gauss(A))
