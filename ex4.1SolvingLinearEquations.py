# Write a function to solve linear equations.
'''
For any form of linear equation;
ax + b = cx + d
ax - cx = d - b
x (a - c) = d - b
x = (d - b) / (a - c)
'''
def linearEquation(a, b, c, d):
    return (d-b)/(a-c)