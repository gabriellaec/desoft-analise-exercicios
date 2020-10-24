def raiz_quadrada(numero):
    i=1
    j=0
    while numero>0:
        numero-=i
        i+=2
        j+=1
    return j