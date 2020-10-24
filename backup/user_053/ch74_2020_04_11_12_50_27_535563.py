def identifica_bigramas(sentenca):
    lista_bigramas = []
    for i in range(0, (len(sentenca) - 1)):
        bigrama = sentenca[i] + sentenca[i+1]
        lista_bigramas.append(bigrama)
    return lista_bigramas

def conta_bigramas(lista):
    contagem = dict()
    for bigramas in lista:
        contador = 0
        i = 0
        while i < len(lista):
            if lista[i] == bigramas:
                contador += 1
                i += 1
            else:
                i += 1
        contagem[bigramas] = contador
    return contagem