def quantos_uns(x):
    i=0
    contagem=0
    y=str(x)
    while i<len(y):
        if y[i]=='1':
            contagem+=1
        i+=1
    return(contagem)