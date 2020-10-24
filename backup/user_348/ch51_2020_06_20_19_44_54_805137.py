def primos_entre (a,b):
    primos = []
    p = 2
    while p >= a and p<=b:
        if p == 2:
            primos.append(p)
        if p == 3:
            primos.append(p)
        for i in range (3, p):
            if (p%2 !=0) and (p%i != 0):
                primos.append(p)
                p = p + 1
        p = p + 1
    return primos
            
        
            