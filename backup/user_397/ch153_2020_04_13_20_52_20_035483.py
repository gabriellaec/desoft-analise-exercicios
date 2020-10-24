def agrupa_por_idade(idade):
    grupo = {"crianca":[], "adolescente":[], "adulto":[], "idoso":[]}
    for x in idade:
        if idade[x] <= 11:
            grupo["crianca"].append(x)
        elif idade[x] >= 12 and idade[x] <= 17:
            grupo["adolescente"].append(x)
        elif idade[x] >= 18 and idade[x] <= 59:
            grupo["adulto"].append(x)
        return grupo