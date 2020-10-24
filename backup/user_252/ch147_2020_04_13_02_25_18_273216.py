def conta_ocorrencias(lista):
    d={}
    for i in range(len(lista)):
        palavra=lista[i]
        if palavra in d:
            d[palavra]+=1
        else:
            d[palavra]=1
    return d
def mais_frequnte(x):
    y=mais(x)
    t=0
    for i, v in y.items():
        if v>mais:
            j=i
            mais=v
    return mais
    
    