def agrupa_por_idade(dic_nomeidade):
    dic_faixaetaria={}
    lista_crianca=[]
    lista_adolescente=[]
    lista_adulto=[]
    lista_idoso=[]
    for n in dic_nomeidade.keys():
        
        if dic_nomeidade[n]<=11:
            lista_crianca.append(n)
            
        elif 12<=dic_nomeidade[n]<=17:
            lista_adolescente.append(n)
            
        elif 18<=dic_nomeidade[n]<=59:
            lista_adulto.append(n)
            
        else:
            lista_idoso.append(n)
            
    dic_faixaetaria['criança']=lista_crianca
    dic_faixaetaria['adolescente']=lista_adolescente
    dic_faixaetaria['adulto']=lista_adulto
    dic_faixaetaria['idoso']=lista_idoso
    return dic_faixaetaria