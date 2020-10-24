def arcotangente (x,n):
    a = 1    
    b = 0
    seno = 1
    while a <= n*2:
        c = (seno*(x**a))/a
        a = a + 2
        b = b + c
        seno = -seno
    return b
        
        