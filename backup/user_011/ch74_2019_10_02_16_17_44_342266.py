def conta_bigramas(string):
    dic = {}
    i = 0
    while i < len(string) - 1:
        bigrama = string[i] + string[i+1]
        if bigrama in dic:
            dic[bigrama]+=1
        else:
            dic[bigrama] = 1
        
        i+=1
    return dic

s="banana nanica"
print(conta_bigramas(s))