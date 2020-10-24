def agrupa_por_idade(x):
    idade = {}
    crianca = {}
    adolescente = {}
    adulto = {}
    idoso = {}
    for e in x:
        j = x[e]
        if j <=11:
            div = "Criança"
            crianca.append(e)
            idade[div]=crianca
        elif j>11 and j <=17:
            div = "adolescente"
            adolescente.append(e)
            idade[div] = adolescente
        elif j>17 and j <=59:
            div = "adulto"
            adulto.append(e)
            idade[div] = adulto
        else:
            div = "idoso"
            idoso.append(e)
            idade[div] = idoso
    if "criança" not in idade:
        idade["criança"] = crianca
    elif "adolescente" not in idade:
        idade["adolescente"] = adolescente
    elif "adulto" not in idade:
        idade["adulto"] = adulto
    elif "idoso" not in idade:
        idade["idoso"] = idoso
    return idade       