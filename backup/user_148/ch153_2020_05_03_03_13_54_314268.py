def agrupa_por_idade(dic):
    dic2 = {}
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    
    for k, v in dic.items():
        if v<=11:
            crianca.append(k)
            dic2['criança'] = crianca
        elif 11<v<18:
            adolescente.append(k)
            dic2['adolescente'] = adolescente
        elif 18<=v<60:
            adulto.append(k)
            dic2['adulto'] = adulto
        else:
            idoso.append(k)
            dic2['idoso'] = idoso
    
    return dic2