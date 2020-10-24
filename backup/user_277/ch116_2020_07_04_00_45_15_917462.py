def raiz_quadrada(numero):
    i = 0
    contador = 0
    impares = 1
    while i < numero:
        numero -= impares
        impares +=1
        contador+=1
    return contador