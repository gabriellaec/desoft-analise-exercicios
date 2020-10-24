def conta_letras(S):
    dic = {}
    for i in range(len(S)):
        if S[i] in dic:
            dic[S[i]] = (dic[S[i]]) + 1
        else:
            dic[S[i]] = 1
    return dic    