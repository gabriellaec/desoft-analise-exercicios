def acha_bigramas(frase):
    bigramas = []
    contador = 0
    while contador < len(frase) - 1:
        bigrama = frase[contador] + frase[contador + 1]
        bigramas.append(bigrama)
        contador += 1
    return bigramas

