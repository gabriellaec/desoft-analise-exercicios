def zera_negativos(n):
    a = len(n)
    i=0
    while i < a:
        if a[i] < 0: 
            a[i] == 0
            i+=1
            return a