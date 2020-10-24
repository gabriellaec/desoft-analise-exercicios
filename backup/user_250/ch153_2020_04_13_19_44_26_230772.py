def agrupa_por_idade(lista):
    dict = {}
    dict["criança"] = []
    dict["adolescente"] = []
    dict["adulto"] = []
    dict["idoso"] = []
    for i in lista:
        if lista[i] <= 11:
            dict["criança"].append(i)
        elif lista[i] >= 12 and lista[i] <= 17:
            dict["adolescente"].append(i)
        elif lista[i] >= 18 and lista[i] <= 59:
            dict["adulto"].append(i)
        else:
            dict["idoso"].append(i)
    return dict