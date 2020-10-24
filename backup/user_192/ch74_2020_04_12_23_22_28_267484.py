def conta_bigramas(sentenca):

    lista_bigramas = []
    for i in range(0, (len(sentenca) - 1)):
        bigrama = sentenca[i] + sentenca[i+1]
        lista_bigramas.append(bigrama)

    contagem = dict()
    for bigramas in lista_bigramas:
        contador = 0
        i = 0
        while i < len(lista_bigramas):
            if lista_bigramas[i] == bigramas:
                contador += 1
                i += 1
            else:
                i += 1
        contagem[bigramas] = contador
    return contagem

a = 'Banana nanica'
c = conta_bigramas(a)
print(c)