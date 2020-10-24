def agrupa_por_idade(nome):
    faixa={}
    crianca=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    for n in nome:
        if nome[n]<=11:
            crianca.append(n)
        elif nome[n]> 11 and nome[n]<= 17:
            adolescente.append(n)
        elif nome[n]>17 and nome[n]<=59:
            adulto.append(n)
        else:
            idoso.append(n)
    faixa['criança']=crianca
    faixa['adolescente']=adolescente
    faixa['adulto']=adulto
    faixa['idoso']=idoso
    return faixa