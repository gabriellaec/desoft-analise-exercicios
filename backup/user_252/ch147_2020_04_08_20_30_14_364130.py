def conta_ocorrencias (palavras):
    dicio={}
    i=0
    while i < len(palavras):
        palavra=palavras[i]
        if palavra in dicio:
            dicio[palavra]+=1
        else:
            dicio[palavra]=1
        i+=1
    return dicio
def mais_frequnte (x):
    ocorrencia=conta_ocorrencias(x)
    