def agrupa_por_idade(x):
    dicionario = {}
    for nome, idades in x.items():
        if idades <= 11:
            dicionario["criança"] = [nome]
        elif 12 <= idades <= 17:
            dicionario["adolescente"] = [nome]
        elif 18 <= idades <= 59:
            dicionario["adulto"] = [nome]
        elif idades >= 60:
            dicionario["idoso"] = [nome]
        elif idades <= 11 and criança in dicionario:
            dicionario["criança"] += [nome]
        elif 12 <= idades <= 17 and adolescente in dicionario:
            dicionario["adolescente"] += [nome]
        elif 18 <= idades <= 59 and adulto in dicionario:
            dicionario["adulto"] += [nome]
        elif idades >= 60 and idoso in dicionario:
            dicionario["idoso"] += [nome]
    return dicionario