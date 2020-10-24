def PiWallis(n):
    x = 2
    y = 1
    k = x/y
    for i in range(0, n):
        if i % 2 == 0:
            y += 2
        if i % 2 == 1:
            x += 2
        k = k * x[i]/y[i]        
        return 2*k
