def agrupa_por_idade(dicionario):
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    dicionario2 = {}
    for nome in dicionario.keys():
        if dicionario[nome] <= 11:
            crianca.append(nome)
        elif 12 < dicionario[nome] <= 17:
            adolescente.append(nome)
        elif 17 < dicionario[nome] <= 59:
            adulto.append(nome)
        else:
            idoso.append(nome)
    dicionario2["criança"] = crianca
    dicionario2["adolescente"] = adolescente
    dicionario2["adulto"] = adulto
    dicionario2["idoso"] = idoso
    return dicionario2
          