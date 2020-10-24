def mais_populoso(dic):
    d = {}
    for each in dic:
        d[each] = sum(dic[each].values())
    print(d)
    
    return sorted(d)[0]