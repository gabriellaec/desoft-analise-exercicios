def PiWalls(n):
    n = 0
    d = 0
    pi = 1
    for x in range(1,n):
        if x == 1:
            pi *= n/d
        else:   
            #if x não é divisível por 2
            if x%2 != 0:
                n += 2
                pi *= n/d
            #if x é divisivel por 2
            else:
                d += 2
                pi *= n/d
    return pi*2