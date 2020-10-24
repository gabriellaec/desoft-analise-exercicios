def collatz(x):
    while x<len(collatz):
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
            