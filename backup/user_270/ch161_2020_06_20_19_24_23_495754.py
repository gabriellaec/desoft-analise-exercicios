def PiWallis(n):
    sum = 2
    n = 2
    d = 1
    for x in (1,n+1):
        if x%2 != 0:
            n = n
            d += 2
            sum *= n/d
        else:
            n += 2
            d = d
            sum *= n/d
    return sum*2