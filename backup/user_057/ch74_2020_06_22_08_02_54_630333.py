def conta_bigramas(str):
    dic={}
    for i in str:
        if (str[i]str[i+1]) in dic:
            dic[str[i]str[i+1]] += 1
        else:
            dic[str[i]str[i+1]] = 1
    return dic