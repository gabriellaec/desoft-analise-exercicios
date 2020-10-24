def mais_populoso(dic):
    sp=0
    for t,i in dic.items():
        sm=0
        for m in dic[t].values():
            sm+=m
            if sm>sp:
                sp=sm
                x=t
    return x