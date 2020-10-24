def conta_ocorrencias(lista):
    d={}
    for i in range(len(lista)):
        palavra=lista[i]
        if palavra in d:
            d[palavra]+=1
        else:
            d[palavra]=1
    return d
def mais_frequente(x):
    y=conta_ocorrencias(x)
    t=0
    for i, v in y.items():
        if v>t:
            i=j
            v=t
    return j
    
    