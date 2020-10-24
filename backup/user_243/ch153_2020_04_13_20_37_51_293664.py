def agrupa_por_idade(dic):
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    dic={}
    dic[criança]=lista1
    dic[adolescente]=lista2
    dic[adulto]=lista3
    dic[idoso]=lista4
    for a,b in dic.items():
        if b<11:
            lista1.append(t)
        elif b<17:
            lista2.append(t)
        elif i<59:
            lista3.append(t)
        else:
            lista4.append(t)
    return dic
    