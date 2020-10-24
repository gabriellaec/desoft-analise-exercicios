def agrupa_por_idade(dict1):
    dict2={}
    listac=[]
    listaad=[]
    listaa=[]
    listai=[]
    for k in dict1:
        if dict1[k]<=11:
            listac.append(k)
            dict2['criança']=listac
        elif dict1[k]<=17:
            listaad.append(k)
            dict2['adolescente']=listaad
        elif dict1[k]<=59:
            listaa.append(k)
            dict2['adulto']=listaa
        else:
            listai.append(k)
            dict2['idoso']=listai
    return dict2