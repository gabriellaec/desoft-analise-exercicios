def PiWallis(n):
    pi = 0
    i = 2
    z = 1
    while z <= n:
        pi += i / z
        z += 2
        pi += i / z
        i += 2
    pi *= 2
    
    return pi