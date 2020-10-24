def agrupa_por_idade(dicionario):
    dicionario2 = {}
    for nomes, idades in dicionario.items():
        if idades <= 11:
            dicionario2['criança'] = [nomes]
        elif idades >= 12 and idades <= 17:
            dicionario2['adolescente'] = [nomes]
        elif idades >= 18 and idades <= 59:
            dicionario2['adulto'] = [nomes]
        else:
            dicionario2['idoso'] = [nomes]
    return dicionario2