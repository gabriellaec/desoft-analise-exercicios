def acha_bigramas(frase):
    bigramas = []
    contador = 0
    while contador < len(frase) - 1:
        bigrama = frase[contador] + frase[contador + 1]
        if bigrama not in bigramas:
            bigramas.append(bigrama)
        contador += 1
    return bigramas

