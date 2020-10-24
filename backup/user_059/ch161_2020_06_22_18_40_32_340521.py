def PiWallis(n):
    num = 2
    den = 1 
    i = 0
    meiopi = 1
    while i<n:
        meiopi *= num/den
        if i%2 == 0: 
            den += 2
        else:
            num += 2
        i+=1
    return 2*meiopi