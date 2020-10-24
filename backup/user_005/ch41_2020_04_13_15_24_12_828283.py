def zera_negativos(n):
    i=0
    while i < len(n):
        if n[i] < 0: 
            n[i] = 0
        i+=1
    return n
        