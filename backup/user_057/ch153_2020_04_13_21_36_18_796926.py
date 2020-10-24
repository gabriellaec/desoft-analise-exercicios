def agrupa_por_idade(dic):
    criança=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    resposta= {}  
    for i in dic.values:
        if i <= 11:
            criança.append(dic[i])
        elif 11 < i <= 17:
            adolescente.append(dic[i])    
        elif 17 < i <= 59:
            adulto.append(dic[i])
        elif 59 < i :
            idoso.append(dic[i])  
    resposta['criança'] = criança  
    resposta['adolescente'] = adolescente
    resposta['adulto'] = adulto
    resposta['idoso'] = idoso
    return resposta
