def  agrupa_por_idade(dicionario):
    dicionario2={}
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    for i in dicionario:
        if i not in dicionario2:
            if dicionario[i]<=11:
                lista1.append(i)
                dicionario2['criança']=lista1
            if dicionario[i]>=12 and dicionario[i]<=17:
                lista2.append(i)
                dicionario2['adolescente']=lista2
            if dicionario[i]>=18 and dicionario[i]<=59:
                lista3.append(i)
                dicionario2['adulto']=lista3
            if dicionario[i]>=60:
                lista4.append(i)
                dicionario2['idoso']=lista4

    return dicionario2