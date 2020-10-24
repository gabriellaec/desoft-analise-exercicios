def agrupa_por_idade(dicionario):
    lista_crianca = []
    lista_adolescente = []
    lista_adulto = []
    lista_idoso = []
    
    dicionario['criança'] = lista_crianca
    dicionario['adolescente'] = lista_adolescente
    dicionario['adulto'] = lista_adulto
    dicionario['idoso'] = lista_idoso
    
    for a, b in dicionario.items():
        if b <= 11:
            lista_crianca.append(a)
        elif b <= 17:
            lista_adolescente.append(a)
        elif b <= 5:
            lista_adulto.append(a)
        else:
            lista_idoso.append(a)
    return dicionario