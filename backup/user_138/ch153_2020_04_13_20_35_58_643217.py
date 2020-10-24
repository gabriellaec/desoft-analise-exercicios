def agrupa_por_idade(dict1):
    dict2={}
    listac=[]
    listaad=[]
    listaa=[]
    listai=[]
    for k in dict1.values():
        if k<=11:
            listac.append(dict1.keys(k))
            dict2['criança']=listac
        elif k<=17:
            listaad.append(dict1.keys(k))
            dict2['adolescente']=listaad
        elif k<=59:
            listaa.append(dict1.keys(k))
            dict2['adulto']=listaa
        else:
            listai.append(dict1.keys(k))
            dict2['idoso']=listai
    return dict2