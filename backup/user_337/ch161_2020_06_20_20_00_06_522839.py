def PiWallis(n):
    mult = 1
    for i in range(1, n+1):
        if i%2 == 0:
            mult = mult * ((i)/(i+1))
        else:
            mult = mult * ((i+1)/(i))
    return mult*2