def conta_bigramas(string):
    dicionario={}
    i=1
    for bigrama in string:
        bigrama=string[i-1]+string[i]
        if not bigrama in dicionario:
            dicionario[bigrama]=string.count(bigrama)
        i+=1
    return dicionario