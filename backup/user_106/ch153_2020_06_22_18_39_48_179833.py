def agrupa_por_idade(nomes):
    for n in nomes:
        if nomes[n] <= 11:
            faixa[crianca].append(n)
        elif 12 <= nomes[n] <= 17:
            faixa[adolescente].append(n)
        elif 18 <= nomes[n] <= 59:
            faixa[adulto].append(n)
        else:
            faixa[idoso].append(n)
    return faixa


'''

def agrupa_por_idade(nome):
    idade = {}
    for n in nome:
        if nome[n] in idade:
            idade[nome[n]].append(n)
        else:
            idade[nome[n]] = [n]
    return idade