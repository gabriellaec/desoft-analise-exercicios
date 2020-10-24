def agrupa_por_idade(dic):
    dic2 = {}
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    
    for k, v in dic.items():
        if v<=11:
            crianca.append(k)
        elif 11<v<18:
            adolescente.append(k)
        elif 18<=v<60:
            adulto.append(k)
        else:
            idoso.append(k)
            
    dic2['idoso'] = idoso
    dic2['adulto'] = adulto
    dic2['adolescente'] = adolescente
    dic2['criança'] = crianca
    return dic2