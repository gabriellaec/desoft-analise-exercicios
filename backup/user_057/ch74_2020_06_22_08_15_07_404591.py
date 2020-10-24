def conta_bigramas(s):
    dic={}
    for i in range(len(s)-1):
        if str(s[i: i+2]) in dic.keys():
            dic[s[i:i+2]] += 1
        else:
            dic[s[i:i+2]] = 1
    return dic