def conta_letras(string):
    dic = {}
    for i in string:
        if i not in dic:
            dic[i]=1
        else:
            dic[i] += i
    return dic