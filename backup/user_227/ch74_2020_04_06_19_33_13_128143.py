def conta_bigramas(string):
    dicionario={}
    i=0
    for bigrama in string:
        if i<len(string)-1:
            bigrama=string[i]+string[i+1]
            if not bigrama in dicionario:
                dicionario[bigrama]=string.count(bigrama)
            i+=1
    return dicionario