def agrupa_por_idade(dic):
    adt = []
    cri = []
    adl = []
    ido = []
    dic = {}
    chav = dic.keys()
    for i in chav:
        if dic[i] <= 11:
            cri.append(i)
        elif dic[i] >= 60:
            ido.append(i)
        elif 12 <= dic[i] <= 17:
            adl.append(i)
        else:
            adt.append(i)
    dic["criança"] = cri
    dic["adolescente"] = adl
    dic["adulto"] = adt
    dic["idoso"] = ido
    return dic
    
            