def agrupa_por_idade(dicionario):
    listaC=[]
    listaA=[]
    listaAD=[]
    listaI=[]
    c='criança'
    a='adolescente'
    ad='adulto'
    i='idoso'
    dicionario1={}
    dicionario1[c]=listaC
    dicionario1[a]=listaA
    dicionario1[ad]=listaAD
    dicionario1[i]=listaI
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
        
        