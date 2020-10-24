def conta_bigramas(string):
    dic = dict()
    bi = ''
    for i in range(1,len(string)):
        bi = string[i-1] + string[i]
        if bi in dic:
             dic[bi] += 1   
        else:
              dic[bi] = 1
    return dic