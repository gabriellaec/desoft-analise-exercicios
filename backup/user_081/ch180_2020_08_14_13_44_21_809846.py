dicio = {}
def ocorrencias_letras(s):
    for i in s:
        if i in dicio:
            dicio[i]+=1
        else:
            dicio[i]=1
    return dicio