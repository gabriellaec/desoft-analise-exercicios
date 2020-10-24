def mais_populoso(dic):
    counter = 0
    country = 0
    sum = 1
    newdic = {}
    for k,v in dic.items():
        sum = 0
        for i in v.values():
            sum += i
            if sum >= counter:
                country = k
                counter = sum
    return country