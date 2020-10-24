def agrupa_por_idade(idades):
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    dic = {}
    for pessoa in idades:
        if idades[pessoa] <= 11:
            criança.append(pessoa)
        elif idades[pessoa] >= 12 and idades[pessoa] <= 17:
            adolescente.append(pessoa)
        elif idades[pessoa] >= 18 and idades[pessoa] <= 59:
            adulto.append(pessoa)
        elif idades[pessoa] >= 60:
            idoso.append(pessoa)
    dic['criança'] = criança
    dic['adolescente'] = adolescente
    dic['adulto'] = adulto
    dic['idoso'] = idoso
    return dic