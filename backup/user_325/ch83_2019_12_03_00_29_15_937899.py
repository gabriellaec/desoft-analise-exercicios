def medias_por_inicial(dicionario_notas):
    dicionario_medias = {}
    lista_chaves = list(dicionario_notas.keys())
    lista_valores = list(dicionario_notas.values())
    contador = 0

    for nomes in lista_chaves:
        if nomes[0] in dicionario_medias:
            dicionario_medias[lista_chaves[contador][0]] = (lista_valores[contador] + lista_valores[contador-1]) / 2
        else:
            dicionario_medias[lista_chaves[contador][0]] = lista_valores[contador]
        contador += 1
    return dicionario_medias