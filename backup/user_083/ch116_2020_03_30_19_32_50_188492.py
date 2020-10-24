def raiz_quadrada(x):
    s=1
    y=1
    c=0
    while y>0 and x>0:
        c+=1
        y=x-s
        s+=s+2
        return c
print(raiz(9))