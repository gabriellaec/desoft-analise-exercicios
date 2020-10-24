def agrupa_por_idade(dic):
    dic={'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
    k=dic.values()
    for i in k:
        if i<=11:
            dic[i]='criança'
        elif i>11 and i<18:
            dic[i]='adolescente'
        elif i>17 and i<60:
            dic[i]='adulto'
        else:
            dic[i]='idoso'
    return dic
            
            
            