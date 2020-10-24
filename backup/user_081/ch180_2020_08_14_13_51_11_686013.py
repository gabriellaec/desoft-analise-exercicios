
def ocorrencias_letras(s):
    dicio = {}
    for i in s:
        if i in dicio:
            dicio[i]+=1
        else:
            dicio[i]=1
    print (dicio)