def mais_populoso(dic):
    for each in dic:
        dic[each] = sum(dic[each].values())
    
    return sorted(dic)[0]