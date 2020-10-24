def medias_por_inicial(notas_por_nome):
    notas_por_inicial = {}
    for nome in notas_por_nome.keys():
        primeira_letra = nome[0]
        contador = 0
        for nota in notas_por_nome.values():
            if primeira_letra not in notas_por_inicial:
                notas_por_inicial[primeira_letra] = nota
            else:
                notas_por_inicial[primeira_letra] += nota
            contador += 1
        notas_por_inicial[primeira_letra] /= contador
    return notas_por_inicial
                