def PiWallis(num):
    pi = 2
    for n in range(1, num + 1):
        if n % 2 == 0:
            pi = pi * n/(n+1)
        else: 
            pi = pi * (n+1)/n
    return pi