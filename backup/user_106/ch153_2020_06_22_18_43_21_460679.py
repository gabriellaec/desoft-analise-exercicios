def agrupa_por_idade(nomes):
    faixa = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for n in nomes:
        if nomes[n] <= 11:
            faixa['criança'].append(n)
        elif 12 <= nomes[n] <= 17:
            faixa['adolescente'].append(n)
        elif 18 <= nomes[n] <= 59:
            faixa['adulto'].append(n)
        else:
            faixa['idoso'].append(n)
    return faixa