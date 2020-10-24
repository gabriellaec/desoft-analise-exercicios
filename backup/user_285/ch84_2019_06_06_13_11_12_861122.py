def inverte_dicionario(idades):
    dicn={}
    for nome,idade in idades.items():
        if idade not in dicn:
            nomes=[nome]
        else:
            dicn[idades]=nomes
            nomes.append(nome)
        dicn[idade]=nomes
    return dicn