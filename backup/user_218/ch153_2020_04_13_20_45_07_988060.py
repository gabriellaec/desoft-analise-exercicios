def agrupa_por_idade(dicionario):
    lista_crianca = []
    lista_adolescente = []
    lista_adulto = []
    lista_idoso = []
    
    dicionario['crianca'] = lista_crianca
    dicionario['adolescente'] = lista_adolescente
    dicionario['adulto'] = lista_adulto
    dicionario['idoso'] = lista_idoso
    
    for a, idade in dicionario.items():
        if idade <= 11:
            lista_crianca.append(a)
        elif idade <= 17:
            lista_adolescente.append(a)
        elif idade <= 5:
            lista_adulto.append(a)
        else:
            lista_idoso.append(a)
    return dicionario