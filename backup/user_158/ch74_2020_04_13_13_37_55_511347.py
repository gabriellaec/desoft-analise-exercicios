def conta_bigramas (string):
    i=0
    dicionario = {}
    while i <len(string)-1:
        bigrama = string[i:i+2]
        if bigrama in dicionario:
            dicionario[bigrama]+=1
        else:
            dicionario[bigrama]=1
        i+=1
    return dicionario
