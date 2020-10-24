def mais_populoso(dicionario):
    lista_compara = []
    dici = {}
    for keys,dic in dicionario.items():
        total = sum(dic.values())
        dici[keys] = total

    lista = list(dici.values())
    for chave,valores in dici.items():
        if max(lista) == valores:
            return chave