def conta_bigramas(palavra):
    dic ={}
    a = 0
    
    for i in palavra:
        bigrama = palavra[a] + palavra[a+1]
        a+=1
       
        if bigrama not in dic:
            dic[bigrama] = 1
        else:
            dic[bigrama] +=1
    return dic