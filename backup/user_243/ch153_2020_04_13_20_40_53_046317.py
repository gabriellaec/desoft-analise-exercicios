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
            lista1.append(a)
        elif b<=17:
            lista2.append(a)
        elif b<=59:
            lista3.append(a)
        else:
            lista4.append(a)
    return dic1
    