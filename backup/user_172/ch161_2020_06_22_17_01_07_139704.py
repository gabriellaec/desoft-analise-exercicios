def PiWallis(n):
    pi = 1
    while n>0:
        if n%2 == 0:
            x = n/(n+1)
        else:
            x = (n+1)/n
        pi = pi*x
    return pi*2