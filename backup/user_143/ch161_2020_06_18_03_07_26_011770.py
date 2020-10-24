def PiWallis (i):
    x = 2
    c = 2
    p = 0
    pi = 1
    while x <= (i * 2):
        if c%2 == 0 and x%2 == 0:
            pi *= (x / (x - 1))
        else:
            p = x - 1
            pi *= (p / (p + 1))
        x+=1
        c+=1
    return pi * 2
                   