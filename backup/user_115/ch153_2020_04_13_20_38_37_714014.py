def agrupa_por_idade(dicO):
    idade = {}
    numero = [dicO.values()]
    nome = [dicO.keys()]
    for numero in range (0, 12):
        idade['criança'] = nome[numero]
    for numero in range (12, 18):
        idade['adolescente'] = nome[numero]
    for numero in range (18, 60):
        idade['adulto'] = nome[numero]
    for numero in range (60, reverse = True):
        idade['idoso'] = nome[numero]

    return idade