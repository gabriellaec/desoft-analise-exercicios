def inverte_dicionario(dicionario):
    dic = {}
    nomes = list(dicionario.keys())
    for nome in nomes:
        idade = dicionario[nome]
        lista = []
        for nome in nomes:
            if idade == dicionario[nome]:
                lista.append(nome)
        dic[idade] = lista
    return dic