def mais_populoso(dic):
    counter = 0
    country = 0
    sum = 1
    newdic = {}
    for k,v in dic.items():
        if sum > counter:
            country = k
        sum = 0
        for i in v.values():
            sum += i
    return country