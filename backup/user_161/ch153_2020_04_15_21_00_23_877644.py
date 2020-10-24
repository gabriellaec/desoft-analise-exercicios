def agrupa_por_idade(dic):
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    dic2={}
    for k,v in dic.items():
        if v<12:
            a='criança'
            lista1.append(k)
            dic2[a]=lista1
        elif v<18:
            b='adolescente'
            lista2.append(k)
            dic2[b]=lista2
        elif v<60:
            c='adulto'
            lista3.append(k)
            dic2[c]=lista3
        else:
            d='idoso'
            lista4.append(k)
            dic2[d]=lista4
    return dic2