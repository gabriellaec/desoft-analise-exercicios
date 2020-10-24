def agrupa_por_idade(dicionario):
    dicionario1={}
    listaC=[]
    listaA=[]
    listaAD=[]
    listaI=[]
    for t, i in dicionario.items():
        if i<=11:
            listaC.append(t)
            dicionario1[criança]=listaC
        elif i<=17:
            listaA.append(t)
            dicionario1[adolescente]=listaA
        elif i<=59:
            listaAD.append(t)
            adolescente[adulto]=listaAD
        else:
            listaI.append(t)
            adolescente[idoso]=listaI
    return dicionario1
        
        