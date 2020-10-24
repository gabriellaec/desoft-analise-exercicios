def agrupa_por_idade(nome):
    idade = {}
    for n in nome:
        if nome[n] in idade:
            idade[nome[n]].append(n)
        else:
            idade[nome[n]] = [n]
    return idade