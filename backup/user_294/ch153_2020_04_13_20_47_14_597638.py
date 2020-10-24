def agrupa_por_idade(nome):
    faixa={}
    criancas=[]
    adolescentes=[]
    adultos=[]
    idosos=[]
    for n in nome:
        if nome[n]<=11:
            criancas.append(n)
        elif nome[n]> 11 and nome[n]<= 17:
            adolescentes.append(n)
        elif nome[n]>17 and nome[n]<=59:
            adultos.append(n)
        else:
            idosos.append(n)
    faixa['crianca']=crianca
    faixa['adolescentes']=adolescentes
    faixa['adultos']=adultos
    faixa['idosos']=idosos
    return faixa
          