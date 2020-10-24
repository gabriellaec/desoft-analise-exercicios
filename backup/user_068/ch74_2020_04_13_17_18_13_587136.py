def conta_bigramas(a):
    dicionario = {}
    lista = []
    i = 0
    while i < (len(a)-1):
        lista.append(a[i] + a[i+1])
        i+=1
    for t in lista:
        if t in dicionario:
            dicionario[t] += 1
        else:
            dicionario[t] = 1
    return dicionario
#ou
def conta_bigramas(x):
    dicionario = {}
    lista = []
    for t in range(0, len(x)-1):
        lista.append(x[t]+x[t+1])
        
    for i in lista:
        if i in dicionario.keys():
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario











    