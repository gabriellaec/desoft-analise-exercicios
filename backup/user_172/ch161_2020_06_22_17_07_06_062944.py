def PiWallis(n):
    pi = 1
    i = 1
    while n>=i:
        if i%2 == 0:
            x = i/(i+1)
        else:
            x = (i+1)/i
        pi = pi*x
        i+=1
    return pi*2