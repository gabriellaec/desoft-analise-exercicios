def mais_populoso(dic):
    p=0
    sp=0
    for t,i in dic.items():
        for m in dic[t].values():
            p+=m
            if p>sp:
                sp=p
                x=t
    return x