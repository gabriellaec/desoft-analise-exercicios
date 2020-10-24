def agrupa_por_idade(dicio):
    nome=dicio.keys()
    idade=dicio.values()
    listafaxaetaria=[]
    for e in idade:
        if e<=11:
            listafaxaetaria.append('criança')
        elif 11<e<=17:
            listafaxaetaria.append('adolescente')
        elif 17<e<=59:
            listafaxaetaria.append('adulto')
        else:
            listafaxaetaria.append('idoso')
        novodicio=dict(zip(nome,listafaxaetaria))
    diciofinal = {}   
    for key, value in novodicio.items(): 
        if value not in diciofinal: 
            diciofinal[value] = [key] 
        else: 
            diciofinal[value].append(key) 
    return diciofinal
