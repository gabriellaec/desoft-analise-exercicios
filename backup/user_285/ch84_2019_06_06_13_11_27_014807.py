def inverte_dicionario(idades):
    dicn={}
    for nome,idade in idades.items():
        if idade not in dicn:
            nomes=[nome]
        else:
            nomes=dicn[idade]
            nomes.append(nome)
        dicn[idade]=nomes
    return dicn