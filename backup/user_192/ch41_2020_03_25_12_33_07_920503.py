def zera_negativos(a):
    a_elementos = len(a)
    i = 0 
    while i < a_elementos:
        if a[i] < 0:
            a[i] = 0
        else:
            a[i] = a[i]
        i += 1
    return a 
    
    