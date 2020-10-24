def conta_bigramas(string):
    i=0
    dicionario={}
    while i<(len(string)-1):
        if string[i:i+2] not in dicionario:
            dicionario[string[i:i+2]]=1

        else:
            dicionario[string[i:i+2]]+=1

        i+=1
    return dicionario