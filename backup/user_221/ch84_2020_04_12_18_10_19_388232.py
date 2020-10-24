def inverte_dicionario(nome_idade):
    idade = []
    for nome in nome_idade:
        if nome_idade[nome] not in idade:
            idade.append(nome_idade[nome])
    idade.sort()

    idade_nome = {}
    for nome in idade:
        idade_nome[nome] = []
    for nome in nome_idade:
        for j in idade_nome:
            if j == nome_idade[nome]:
                idade_nome[j].append(nome)
    return idade_nome