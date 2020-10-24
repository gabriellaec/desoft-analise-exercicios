def agrupa_por_idade(dic):
    faixaEtaria = {}
    faixaEtaria['criança'] = []
    faixaEtaria['adolescente'] = []
    faixaEtaria['adulto']= []
    faixaEtaria['idoso'] = []
    for n, i in dic.items():
        if i <= 11:
            faixaEtaria['criança'].append(n)
        elif 12 <= i <= 17:
            faixaEtaria['adolescente'].append(n)
        elif 18 <= i <= 59:
            faixaEtaria['adulto'].append(n)
        else:
            faixaEtaria['idoso'].append(n)
    return faixaEtaria
