def conta_bigramas(palavra):
    dicionario = {}
    bigrama=[]
    for i in range(0, len(palavra)-1):
        if i==len(palavra)-1:
            break
        else:
            bigramavar = palavra[i] + palavra[i+1]
            bigrama.append(bigramavar)
    for i in range(0, len(palavra)-1):
        if i==len(palavra)-1:
            break
        else:
            bigramavar = palavra[i] + palavra[i+1]
            dicionario[bigramavar]=0
    for i in bigrama:
        dicionario[i]+=1
    return dicionario