def agrupa_por_idade(dicionario):
    lista_de_criancas = []
    lista_de_adolescente = []
    lista_de_adultos = []
    lista_de_idosos = []
    novo_dicionario = {'criança': lista_de_criancas, 'adolescente': lista_de_adolescente, 'adulto': lista_de_adultos, 'idoso': lista_de_idosos}

    for chave in dicionario.keys():
        if dicionario[chave] <= 11:
            lista_de_criancas.append(chave)
        elif dicionario[chave] >= 12 and dicionario[chave] <= 17:
            lista_de_adolescente.append(chave)
        elif dicionario[chave] >= 18 and dicionario[chave] <= 59:
            lista_de_adultos.append(chave)
        elif dicionario[chave] >= 60:
            lista_de_idosos.append(chave)
    
    return novo_dicionario