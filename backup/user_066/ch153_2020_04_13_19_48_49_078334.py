def agrupa_por_idade(dicionario):
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    for i,j in dicionario.items():
        if j <= 11:
            crianca.append(i)
        elif j <= 17:
            adolescente.append(i)
        elif j <= 59:
            adulto.append(i)
        else:
            idoso.append(i)
    dicionario_agrupado = {'criança':crianca,'adolescente':adolescente,'adulto':adulto,'idoso':idoso}
    return dicionario_agrupado