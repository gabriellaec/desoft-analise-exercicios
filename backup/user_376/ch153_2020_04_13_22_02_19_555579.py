def  agrupa_por_idade(l):
    i=0
    nomes=l.keys
    listafinal={}
    while len(l)>i:
        nome=nomes[i]
        if l[i]<=11:
            listafinal["criança"]=nome
        elif 12<=l[i]<=17:
            listafinal["adolescente"]=nome
        elif 18<=l[i]<=59:
            listafinal["adulto"]=nome
        elif 60<=l[i]:
            listafinal["idoso"]=nome
        i+=1
    return listafinal