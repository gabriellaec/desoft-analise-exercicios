def agrupa_por_idade(nome_idade):
    fe_idade = {}
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    for e in nome_idade:
        i = nome_idade[e]
        if i <= 11:
            cat = "criança"
            crianca.append(e)
            fe_idade[cat] = crianca
        elif i > 11 and i <= 17:
            cat = "adolescente"
            adolescente.append(e)
            fe_idade[cat] = adolescente
        elif i > 17 and i <= 59:
            cat = "adulto"
            adulto.append(e)
            fe_idade[cat] = adulto
        else:
            cat = "idoso"
            idoso.append(e)
            fe_idade[cat] = idoso
    if "criança" not in fe_idade:
        fe_idade["criança"] = crianca
    elif "adolescente" not in fe_idade:
        fe_idade["adolescente"] = adolescente
    elif "adulto" not in fe_idade:
        fe_idade["adulto"] = adulto
    elif "idoso" not in fe_idade:
        fe_idade["idoso"] = idoso
    return fe_idade