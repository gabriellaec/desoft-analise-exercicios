def agrupa_por_idade(dicionario):
    listaC=[]
    listaA=[]
    listaAD=[]
    listaI=[]
    dicionario1={}
    dicionario1[o]=listaC
    dicionario1[adolescente]=listaA
    dicionario1[adulto]=listaAD
    dicionario1[idoso]=listaI
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
        
        