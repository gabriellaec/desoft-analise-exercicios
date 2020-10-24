def collatz(x):
    while x>1:
        if x%2==0:
            n=n/2
        else:
            n=3*n+1
