def PiWallis(n):
    n = 2
    d = 1
    sum = 1
    if n == 1:
        return 4.0
    else:
        for i in range(0,n+1):
            sum *= n/d
            if i % 2 == 0:
                d += 2
            else:
                n += 2
        return sum*2