listac = ["primeiro","segundo","terceiro"]
listav = ["1","2","3"]
def monta_dicionario(x,y):
    dicionario = {}
    for e in range(len(x)):
        dicionario[x[e]] = y[e]
    return dicionario
print (monta_dicionario(listac, listav))
        