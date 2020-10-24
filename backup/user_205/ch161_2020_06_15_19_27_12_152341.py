def PiWallis(n):
    i = 1
    pi = 1
    while i<=n:
        print(pi)
        if i % 2 == 0: 
            pi *= i/(i+1)
        else:
            pi *= (i+1)/i
        i += 1
        
    return 2*pi
