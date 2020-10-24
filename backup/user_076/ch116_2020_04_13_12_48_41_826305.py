def raiz_quadrada (x):
    i = 1
    c = 0
    while x!=0:
        c+=1
        x-=i
        i+=2
    return c