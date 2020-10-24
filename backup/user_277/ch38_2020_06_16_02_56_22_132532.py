def quantos_uns(k):
    numero = str(k)
    i = 0
    contador = 0
    while i<numero:
        if numero[i]==1:
            contador+=1
    return contador