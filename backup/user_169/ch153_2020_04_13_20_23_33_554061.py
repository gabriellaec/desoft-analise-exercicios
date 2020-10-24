def  agrupa_por_idade(dicionario):
    dicionario2={}
    for i in dicionario:
        if dicionario[i] not in dicionario2:
            if dicionario[i]<=11:
                dicionario2['criança']=[i]
            elif dicionario[i]>=12 and dicionario[i]<=17:
                dicionario2['adolescente']=[i]
            elif dicionario[i]>=18 and dicionario[i]<=59:
                dicionario2['adulto']=[i]
            elif dicionario[i]>=60:
                dicionario2['idoso']=[i]
            
    return dicionario2