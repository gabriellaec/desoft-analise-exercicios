def raiz_quadrada(n):
    i=1
    contador=0
    while n>=i:
        n=n-i
        i+=2
        contador+=1
    return contador