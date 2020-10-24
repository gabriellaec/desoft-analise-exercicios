def raiz_quadrada(x):
    s=1
    y=1
    while y>0:
        y=x-s
        s+=s+2
    print(raiz_quadrada(9))