def raiz_quadrada(n):
    i=1
    contagem=0
    while n>0:
        n-=i
        contagem+=1
        i+=2
    return contagem   