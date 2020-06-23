# Find the sum of l numbers from 1 to a given number.

def FindSum(maxLimit=100):
    summ=0
    for i in range(maxLimit):
        summ+=(i+1)
    return summ
