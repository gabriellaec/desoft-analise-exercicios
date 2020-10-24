def inverte_dicionario(nome):
    idade = dict()
    for i in nome:
        if nome[i] not in idade:
            idade[nome[i]] = [i]
        else:
            idade[nome[i]] = [idade[nome[i]], i]
    return idade