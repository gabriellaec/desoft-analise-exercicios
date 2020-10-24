def raiz_quadrada(numero):
    resultado=0
    i=1
    while i<=numero:
        numero-=i
        resultado+=1
        i+=2
    return resultado