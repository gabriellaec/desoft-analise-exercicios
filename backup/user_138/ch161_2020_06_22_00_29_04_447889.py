def PiWallis (n):
    x = 1
    for i in range (1, n+1):
        if i %2 == 0:
            x *= i/i+1
        else:
            x *= i+1/i
    y = 2*x
    return y