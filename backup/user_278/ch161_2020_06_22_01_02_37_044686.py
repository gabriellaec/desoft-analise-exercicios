def PiWallis(x):
    n=2
    d=1
    pi=2
    for x in range(1,x):
        if x%2!=0:
            n+=2
            pi*=(n/d)
        else:
            d+=2
            pi*=(n/d)
    return pi*2
            