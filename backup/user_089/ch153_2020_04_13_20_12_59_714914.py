def agrupa_por_idade(dic):
    novo = {}
    for e,v in dic.items():
        if v <= 11:
            novo["criança"] = e
        if 12 <= v <= 17:
            novo["adolescente"] = e
        if 18 <= v <= 59:
            novo["adulto"] = e
        if v >= 60:
            novo["idoso"] = e
    return novo
        