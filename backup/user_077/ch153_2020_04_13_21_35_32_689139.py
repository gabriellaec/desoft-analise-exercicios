def agrupa_por_idade(dicionario):
    a=[]
    b=[]
    c=[]
    d=[]
    for e in dicionario:
        if dicionario[e]<12:
            a.append(e)
        elif dicionario[e]>=12 and dicionario[e]<=17:
            b.append(e)
        elif dicionario[e]>=18 and dicionario[e]<=59:
            c.append(e)
        else:
            d.append(e)
        faixas_etarias={'criança':a,'adolescente':b,'adulto':c,'idoso':d}
        return faixas_etarias
            