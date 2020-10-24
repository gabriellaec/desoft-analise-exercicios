def acha_bigramas(frase):
    bigramas = []
    contador = 0
    while contador < len(frase) - 1:
        bigrama = frase[contador] + frase[contador + 1]
        bigramas.append(bigrama)
        contador += 1
    return bigramas

def conta_bigramas(frase):
    lista_bigramas = acha_bigramas(frase)
    numero_bigramas = {}
    contador = 0
    while contador < len(lista_bigramas):
        bigrama = lista_bigramas[contador]
        if bigrama not in numero_bigramas:
            numero_bigramas[bigrama] = 1
        else:
            numero_bigramas[bigrama] += 1
        contador += 1
    return numero_bigramas