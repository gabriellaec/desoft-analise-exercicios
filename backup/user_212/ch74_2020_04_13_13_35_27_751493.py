def conta_bigramas (string):
    i=1
    u=0
    dic={}
    while u<len(string):
        soma= sum(string[i,u])
        if (soma) in dic:
            values = string.count(soma)
            dic[soma] = values
        else:
            dic[soma] = 1
        i+=1
        u+=1

    return dic 
            
    