def agrupa_por_idade(dicionario):
    dicionario1={'criança': [listaC], 'adolescente': [listaA], 'adulto': [listaAD], 'idoso': [listaI]}
    listaC=[]
    listaA=[]
    listaAD=[]
    listaI=[]
    for t, i in dicionario.items():
        if i<=11:
            listaC.append(t)
        elif i<=17:
            listaA.append(t)
        elif i<=59:
            listaAD.append(t)
        else:
            listaI.append(t)
    return dicionario1
        
        