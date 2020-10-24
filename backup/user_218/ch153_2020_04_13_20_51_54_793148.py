def agrupa_por_idade(dicionario):
    lista_crianca = []
    lista_adolescente = []
    lista_adulto = []
    lista_idoso = []
    
    dicionario_novo = {}
    dicionario_novo['criança'] = lista_crianca
    dicionario_novo['adolescente'] = lista_adolescente
    dicionario_novo['adulto'] = lista_adulto
    dicionario_novo['idoso'] = lista_idoso
    
    for a, b in dicionario.items():
        if b <= 11:
            lista_crianca.append(a)
        elif b <= 17:
            lista_adolescente.append(a)
        elif b <= 5:
            lista_adulto.append(a)
        else:
            lista_idoso.append(a)
    return dicionario_novo