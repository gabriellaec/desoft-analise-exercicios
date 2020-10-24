def conta_letras (x):
    dic={}
    for e in x:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
      
    return dic    