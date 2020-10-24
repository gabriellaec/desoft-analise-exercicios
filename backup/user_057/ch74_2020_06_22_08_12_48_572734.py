def conta_bigramas(s):
    dic={}
    for i in range(len(s)):
        if str(s[i: i+1]) in dic.keys():
            dic[s[i:i+1]] += 1
        else:
            dic[s[i:i+1]] = 1
    return dic