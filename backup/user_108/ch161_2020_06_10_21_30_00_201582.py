def PiWallis(n):
    pi = 1
    for i in range(2,n+2):
        pi *= i/(i-1) if i%2==0 else (i-1)/i
    return pi*2