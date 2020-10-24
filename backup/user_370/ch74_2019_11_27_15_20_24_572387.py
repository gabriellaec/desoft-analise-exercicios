def acha_bigramos(palavra):
    bigramo=[]
    i=0
    while i < len(palavra)-1:
        bgrm = palavra[i]+palavra[i+1]
        bigramo.append(bgrm)
        i+=1
    return bigramo
def conta_bigramas(palavra):
    bigramo=acha_bigramos(palavra)
    dicionario = dict()
    i=0
    while i < len(bigramo):
        if bigramo[i] in dicionario:
            dicionario[bigramo[i]]+=1
        else:
            dicionario[bigramo[i]]=1
        i+=1
    return dicionario