def conta_letras(s):
    dic = {}
    for each in s:
        if each not in dic:
            dic[each] = s.count(each)
    return sorted(dic)