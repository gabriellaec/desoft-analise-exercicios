def medias_por_inicial(dic):
    saida = {}
    cont = {}
    for key, values in dic.items():
        letra = key[0]
        if letra not in saida:
            saida[letra] = values
            cont[letra] = 1
        else:
            cont[letra] += 1
            saida[letra] += values
    for key in saida:
        saida[key] = saida[key]/cont[key]
    return saida
    