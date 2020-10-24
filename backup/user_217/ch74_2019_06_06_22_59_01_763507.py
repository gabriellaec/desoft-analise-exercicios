def conta_bigramas(palavra):
    i=0
    dic={}
    while i < len(palavra):
        bigrama = palavra[i] + palavra[i+1]
        if bigrama in dic:
            dic[bigrama] +=1
        else:
            dic[bigrama] = 1
		i+=1
    return dic