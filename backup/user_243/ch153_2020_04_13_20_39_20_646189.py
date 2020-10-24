def agrupa_por_idade(dic):
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    dic1={}
    dic1[criança]=lista1
    dic1[adolescente]=lista2
    dic1[adulto]=lista3
    dic1[idoso]=lista4
    for a,b in dic.items():
        if b<=11:
            lista1.append(t)
        elif b<=17:
            lista2.append(t)
        elif i<=59:
            lista3.append(t)
        else:
            lista4.append(t)
    return dic1
    