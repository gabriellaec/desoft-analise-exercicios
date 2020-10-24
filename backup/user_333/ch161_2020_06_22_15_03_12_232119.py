def PiWallis (n):
    pi2 = 1
    if n == 1:
        pi = 4
    else:
        for e in range(1,n):
            if e % 2 == 0:
                pi2 *= e/(e+1)
            else:
                pi2 *= (e+1)/e
    pi = pi2*2
    return pi