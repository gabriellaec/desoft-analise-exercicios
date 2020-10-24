def conta_bigramas(string):
    dicionario={}
    i=0
    for bigrama in string:
        bigrama=string[i]+string[i+1]
        if not bigrama in dicionario:
            dicionario[bigrama]=string.count(bigrama)
        i+=1
    return dicionario