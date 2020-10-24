def raiz_quadrada (n):
    i=1
    d=n
    c=0
    while i<d:
        d-=i
        i+=2
        c+=1
    return c
        