def agrupa_por_idade(dicionario):
    a = dict()
    a["criança"] = []
    a["adolescente"] = []
    a["adulto"] = []
    a["idoso"] = []
    for nome in dicionario:
        if dicionario[nome] <= 11:
            a["criança"] += dicionario[nome]
        if dicionario[nome] <= 17:
            a["adolescente"] += dicionario[nome]
        if dicionario[nome] <= 59:
            a["adulto"] += dicionario[nome]
        if dicionario[nome] >= 60:
            a["idoso"] += dicionario[nome]
    return a