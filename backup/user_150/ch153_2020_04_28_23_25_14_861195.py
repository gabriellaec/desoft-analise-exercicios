def agrupa_por_idade(dicionario):
    dicionario2 = {'criança':[],'adolescente':[],'adulto':[],'idoso':[]}
    for nomes, idades in dicionario.items():
        if dicionario[nomes] <= 11:
            dicionario2['criança'].append(nomes)
        elif dicionario[nomes] >= 12 and dicionario[nomes] <= 17:
            dicionario2['adolescente'].append(nomes)
        elif dicionario[nomes] >= 18 and dicionario[nomes] <= 59:
            dicionario2['adulto'].append(nomes)
        else:
            dicionario2['idoso'].append(nomes)
    return dicionario2