def conta_bigramas(a):
    dicionario={}
    lista = []
    for bigrama in range(0, len(a)-1):
        lista.append(a[bigrama]+a[bigrama+1])
    for j in a:
        if j in dicionario.keys():
            dicionario[j]+=1
        else:
            dicionario[j]=1
    return dicionario