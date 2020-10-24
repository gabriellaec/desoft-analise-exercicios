def agrupa_por_idade(x):
    dicionario = {}
    for nome, idades in x.items():
        if idades <= 11:
            dicionario[criança] = [nome]
        elif 12 <= idades <= 17:
            dicionario[adolescente] = [nome]
        elif 18 <= idades <= 59:
            dicionario[adulto] = [nome]
        else:
            dicionario[idoso] = [nome]
    return dicionario