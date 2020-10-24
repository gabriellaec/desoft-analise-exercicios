def inverte_dicionario(nome_idade):
    lista_idade = []
    for nome in nome_idade:
        if nome_idade[nome] not in lista_idade:
            lista_idade.append(nome_idade[nome])
    lista_idade.sort()

    idade_nome = {}
    for idade in lista_idade:
        idade_nome[idade] = []
    for nome in nome_idade:
        for idade in idade_nome:
            if idade == nome_idade[nome]:
                idade_nome[idade].append(nome)
    return idade_nome