def raiz_quadrada(numero):
    i = 0
    numero_fixo = numero
    contador = 0
    impares = 1
    while i < numero_fixo:
        numero -= impares
        impares +=1
        contador+=1
        i+=1
    return contador