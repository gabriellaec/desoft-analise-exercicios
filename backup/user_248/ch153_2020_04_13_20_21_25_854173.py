def agrupa_por_idade(dic):
    dic={'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
    dic2=dic
    k=dic.values()
    for i in k:
        if i<=11:
            dic2[i]='criança'
        elif i>11 and i<18:
            dic2[i]='adolescente'
        elif i>17 and i<60:
            dic2[i]='adulto'
        else:
            dic2[i]='idoso'
    return dic2
            
            