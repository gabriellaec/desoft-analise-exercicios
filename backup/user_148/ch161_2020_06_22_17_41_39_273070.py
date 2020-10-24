def PiWallis(n):
    x = 2
    y = 1
    k = x/y
    for i in range(1, n+1):
        k *= x/y
        if i % 2 == 0:
            x += 2
        else:
            y += 2        
    return 2*k