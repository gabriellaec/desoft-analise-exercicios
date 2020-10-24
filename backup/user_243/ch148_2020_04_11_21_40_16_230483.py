def conta_letras(string):
    dic={}
    for t in string:
        if t in dic:
            dic[t]+=1
        else:
            dic[t]=1
    return 
        