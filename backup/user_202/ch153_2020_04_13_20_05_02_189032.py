def agrupa_por_idade(dic_nomes):
    faixa_etaria = {}
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    for k,v in dic_nomes.items():
        if v <= 11: 
            criança.append(k)
        elif v >= 12 and v <= 17: 
            adolescente.append(k)
        elif v >= 18 and v <= 59: 
            adulto.append(k)
        else:
            idoso.append(k)
    faixa_etaria['criança'] = criança
    faixa_etaria['adolescente'] = adolescente
    faixa_etaria['adulto'] = adulto
    faixa_etaria['idoso'] = idoso
    return faixa_etaria
    