def adrupa_por_idade(idd):
    dicionario={}
    agrp={}
    agrp=['crianca', 'adolescente', 'adulto', 'idoso']
    crianca=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    for idd in dicionario:
        if idd>=11:
            crianca.append(dic[idd])
        elif idd>11 and idd<=17:
            adolescente.append(dic[idd])
        elif idd>17 and idd<=18:
            adulto.append(dic[idd])
        else:
            idoso.append(dic[idd])
        print (agrp)