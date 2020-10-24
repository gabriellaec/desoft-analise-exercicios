def mais_populoso(dic):
    p=0
    sm=0
    sp=0
    for t,i in dic.items():
        for m in dic[t].values():
            sm+=m
            if sm>sp:
                sp=sm
                x=t
    return x