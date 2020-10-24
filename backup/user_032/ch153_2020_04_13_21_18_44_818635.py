def agrupa_por_idade(dicionario):
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    for i in dicionario:
        idade = dicionario[i]
        if idade <= 11:
            criança.append(dicionario[i])
        elif idade > 11 and idade < 18:
            adolescente.append(dicionario[i])
        elif idade >= 18 and idade < 60:
            adulto.append(dicionario[i])
        else:
            idoso.append(dicionario[i])
    return ('criança {0}'.format(criança)
    return ('adolescente {0}'.format(adolescente))
    return ('adulto {0}'.format(adulto))
    return ('idoso {0}'.format(idoso))
