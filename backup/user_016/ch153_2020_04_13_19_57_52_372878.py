def agrupa_por_idade(dicionario1):
    dicionario2 = {}
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    for i in dicionario1.keys():
        if dicionario1[i] <= 11:
            lista1.append(i) 
        elif 12 <= dicionario1[i] <= 17:
            lista2.append(i)
        elif 18 <= dicionario1[i] <= 59:
            lista3.append(i)
        else:
            lista4.append(i)
    dicionario2['criança'] = lista1
    dicionario2['adolescente'] = lista2
    dicionario2['adulto'] = lista3
    dicionario2['idoso'] = lista4
    return dicionario2     
            