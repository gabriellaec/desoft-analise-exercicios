def agrupa_por_idade(d):
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    agrupado = {'criança':0,'adolescente':0,'adulto':0,'idoso':0}
    for i in d:
        if d[i] <= 11:
            crianca.append(i)
        elif d[i] > 11 and d[i] < 18:
            adolescente.append(i)
        elif d[i] > 17 and d[i] < 60:
            adulto.append(i)
        else:
            idoso.append(i)
    agrupado['crianca']=crianca
    agrupado['adolescente']=adolescente
    agrupado['adulto']=adulto
    agrupado['idoso']=idoso
    return agrupado