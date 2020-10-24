def agrupa_por_idade(dicionario):
    saida = dict()
    crianca = list()
    adolescente = list()
    adulto = list()
    idoso = list()
    for i in dicionario.keys():
        if dicionario[i] <= 11:
            crianca.append(i)
        elif dicionario[i] >= 12 and dicionario[i] <= 17:
            adolescente.append(i)
        elif dicionario[i] >= 18 and dicionario[i] <= 59:
            adulto.append(i)
        else:
            idoso.append(i)
    saida = {'criança': crianca, 'adolescente':adolescente, 'adulto':adulto, 'idoso':idoso}
    return saida