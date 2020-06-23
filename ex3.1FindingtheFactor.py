# Find the average of numbers in a list.

def GCF(number1, number2):
    gcf=2
    for i in range(2, int(min(number1, number2))):
        if number1%i==0 and number2%i==0:
            gcf=i
    return gcf