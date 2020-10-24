def mais_populoso(dic):
    d = {}
    for each in dic:
        d[each] = sum(dic[each].values())

    return list({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})[0]