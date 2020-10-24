def inverte_dicionario(nome_idade):
    idade_nome={}
    for n,i in nome_idade.items():
        if i not in idade_nome:
            idade_nome[i] = []
        idade_nome[i].append(n)
    return idade_nome
        