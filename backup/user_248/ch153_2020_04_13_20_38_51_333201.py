def agrupa_por_idade(dic):
    dic2={}
    k=dic.values()
    for i in k:
        if i<=11:
            'crianca'=dic2[key]
        elif i>11 and i<18:
            'adolescente'=dic2[key]
        elif i>17 and i<60:
            'adulto'=dic2[key]
        else:
            'idoso'=dic2[key]
    return dic2
            
            