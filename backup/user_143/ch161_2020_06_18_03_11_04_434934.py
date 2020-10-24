def PiWallis (i):
    x = 2
    c = 2
    co = 0
    p = 0
    pi = 1
    while co < i:
        if c%2 == 0 and x%2 == 0:
            pi *= (x / (x - 1))
        else:
            p = x - 1
            pi *= (p / (p + 1))
        x+=1
        c+=1
        co+=1
    return pi * 2
                   