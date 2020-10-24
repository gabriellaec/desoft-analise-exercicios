def conta_bigramas(palavra):
    i=0
    dic={}
    while i < len(palavra):
        if palavra[i] + palavra[i+1] in dic:
            dic[palavra[i] + palavra[i+1]] +=1
        else:
            dic[palavra[i] + palavra[i+1]] = 1
      	i+=1
    return dic