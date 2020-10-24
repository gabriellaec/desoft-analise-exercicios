def agrupa_por_idade(dict1):
    dict2={}
    lista=[]
    for k in dict1.keys():
        if k<=11:
            lista.append(k)
            dict2['criança']=lista
        elif k<=17:
            lista.append(k)
            dict2['adolescente']=lista
        elif k<=59:
            lista.append(k)
            dict2['adulto']=lista
        else:
            lista.append(k)
            dict2['idoso']=lista
    return dict2