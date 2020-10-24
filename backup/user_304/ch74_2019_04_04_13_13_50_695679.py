def conta_bigramas(palavra):
    saida={}
    i=0
    while i<len(palavra)-1:
        bigrama=palavra[i]+palavra[i+1]
        if bigrama not in saida:
            saida[bigrama]=1
        else:
            saida[bigrama]+=1
        i+=1
    return saida