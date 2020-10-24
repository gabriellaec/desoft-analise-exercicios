def inverte_dicionario(nome_idade):
    idade_nome = dict()
    for nome in nome_idade:
        if nome_idade[nome] not in idade_nome:
            idade_nome[nome_idade[nome]] = list(nome)
        else:
            list(idade_nome[nome_idade[nome]]).append(nome)
    return idade_nome