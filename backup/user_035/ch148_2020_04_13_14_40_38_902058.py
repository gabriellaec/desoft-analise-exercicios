def conta_letras(string):
    dic = {}
    i = 0
    while i <= len(string)-1:
        if string[i] not in dic:
            dic[string[i]] = 1
            i += 1
        else:
            dic[string[i]] += 1
            i += 1
    return dic 