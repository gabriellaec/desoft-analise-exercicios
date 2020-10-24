def PiWallis(n):
    pi = 4

    for i in range(1,n):
        if i%2 != 0:
            pi *= (i+1)/i
            
        if i%2 == 0:
            pi *= i/(i+1)

    return pi