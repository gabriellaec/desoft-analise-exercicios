def agrupa_por_idade(x):
    dicionario = {"criança": [], "adolescente": [], "adulto": [], "idoso": []}
    for nome, idades in x.items():
        if idades <= 11:
            dicionario["criança"] += [nome]
        elif 12 <= idades <= 17:
            dicionario["adolescente"] += [nome]
        elif 18 <= idades <= 59:
            dicionario["adulto"] += [nome]
        elif idades >= 60:
            dicionario["idoso"] += [nome]
    return dicionario