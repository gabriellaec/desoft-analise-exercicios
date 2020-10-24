def PiWallis(n):
    pi = 2

    for i in range(1,n+1):
        if i%2 != 0:
            pi *= (i+1)/i
            
        if i%2 == 0:
            pi *= i/(i+1)
    print(i)

    return pi