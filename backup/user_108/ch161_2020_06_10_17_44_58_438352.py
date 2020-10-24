def PiWallis(n):
    pi = 1
    for i in range(2,n+2):
        if i%2 == 0:
            pi *= i/(i-1)
        else:
            print(i-1,i)
            pi *= (i-1)/i
    return pi*2
        