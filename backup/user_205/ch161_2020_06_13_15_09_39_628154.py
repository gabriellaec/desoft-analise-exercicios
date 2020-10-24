def PiWallis(n):
    i = 0 
    z = 2
    k = 1
    pi = 1
    while i<n:
        pi *= (z**2)/(k**2) * n
        return 2*pi