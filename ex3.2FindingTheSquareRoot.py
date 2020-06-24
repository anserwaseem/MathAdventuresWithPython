# Find the square root

def average(a, b):
    return(a+b)/2

def squareRoot(num, low, high):
    for i in range(100):
        guess=average(low, high)
        if guess**2 > num:
            high=guess
        elif guess**2 < num:
            low=guess
        else:
            break
    print(guess)