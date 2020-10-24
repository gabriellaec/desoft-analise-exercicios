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
        diciof={}
        
        for key, value in novodicio.items(): 
            if value not in diciof: 
                diciof[value] = [key] 
            else: 
                diciof[value].append(key) 
                
    if 'criança' not in diciof.keys():
            diciof.update({'criança':[]})
    if 'adolescente' not in diciof.keys():
            diciof.update({'adolescente':[]})
            
    if 'adulto' not in diciof.keys():
            diciof.update({'adulto':[]})
            
    if 'idoso' not in diciof.keys():
            diciof.update({'idoso':[]})
            
    return diciof
            