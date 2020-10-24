def agrupa_por_idade(dicO):
    idade = {}
    for dicO.values() in range (0, 12):
        idade['criança'] = dicO.key()
    for dicO.values() in range (12, 18):
        idade['adolescente'] = dicO.key()
    for dicO.values() in range (18, 60):
        idade['adulto'] = dicO.key()
    for dicO.values() in range (60, reverse = True):
        idade['idoso'] = dicO.key()

    return idade