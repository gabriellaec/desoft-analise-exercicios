def acha_bigramas(string):
    bigramas=[]
    i=0
    while i<len(string)-1:
        bigr=string[i]+string[i+1]
        if not bigr in bigramas:
            bigramas.append(bigr)
        i+=1
    return bigramas

def conta_bigramas(string):
    bigramas=acha_bigramas(string)
    dicionario=dict()
    i=0
    while i<len(bigramas):
        if not bigramas[i] in dicionario:
            dicionario[bigramas[i]]=1
        else:
            dicionario[bigramas[i]]+=1
    return dicionario