
def  agrupa_por_idade(dicionario):
    dicionario2={}
    for i in dicionario:
        if dicionario[i] not in dicionario2:
            if dicionario[i]<=11:
                dicionario2['criança']=[i]
            if dicionario[i]>=12 and dicionario[i]<=17:
                dicionario2['adolescente']=[i]
            if dicionario[i]>=18 and dicionario[i]<=59:
                dicionario2['adulto']=[i]
            if dicionario[i]>=60:
                dicionario2['idoso']=[i]
        else:
            dicionario2[dicionario[i]]+=1    
        
    return dicionario2
