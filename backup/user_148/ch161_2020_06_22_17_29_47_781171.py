def PiWallis(n):
    x = 2
    y = 1
    k = x/y
    for i in range(0, n):
        if n % 2 == 0:
            x += 2
        if n % 2 == 1:
            y += 2
        
    return 2*k
