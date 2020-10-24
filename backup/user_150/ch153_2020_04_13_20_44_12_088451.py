def agrupa_por_idade(dicionario):
    dicionario2 = {}
    for nomes, idades in dicionario.items():
        if dicionario[nomes] <= 11:
            dicionario2['criança'] = [nomes]
        elif dicionario[nomes] >= 12 and dicionario[nomes] <= 17:
            dicionario2['adolescente'] = [nomes]
        elif dicionario[nomes] >= 18 and dicionario[nomes] <= 59:
            dicionario2['adulto'] = [nomes]
        else:
            dicionario2['idoso'] = [nomes]
    return dicionario2

ex = {'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
print(agrupa_por_idade(ex))