def agrupa_por_idade(dic):
    dic={'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
    dic2= dict(map(reversed, my_dict.items()))
    k=dic.values()
    for i in k:
        if i<=11:
            'criança'=dic2[key]
        elif i>11 and i<18:
            'adolescente'dic2[key]
        elif i>17 and i<60:
            'adulto'dic2[key]
        else:
            'idoso'dic2[key]
    return dic2
            
            