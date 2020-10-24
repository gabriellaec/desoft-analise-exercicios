def mais_populoso(dicionario):
    lista_estados = list(dicionario.keys())
    lista_municipios = list(dicionario.values())
    dicionario_estado_populacao = {}
    contador = 0

    for municipios in lista_municipios:
        dicionario_estado_populacao[lista_estados[contador]] = sum(list(municipios.values()))
        contador += 1

    lista_populacao_total = list(dicionario_estado_populacao.values())

    return lista_estados[lista_populacao_total.index(max(lista_populacao_total))]