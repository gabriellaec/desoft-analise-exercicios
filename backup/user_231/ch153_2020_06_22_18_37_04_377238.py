def agrupa_por_idade(d):
    faixas={}
    crianca=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    for k, v, in d.items():
        if v<=11:
            crianca.append(k)
        elif v<=17:
            adolescente.append(k)
        elif v<=59:
            adulto.append(k)
        else:
            idoso.append(k)
    faixas['crianca']=crianca
    faixas['adolescente']=adolescente
    faixas['adulto']= adulto
    faixas['idoso']=idoso
    return faixas