def mais_populoso(brasil):
    for k in brasil.keys():
        s = sum([ int(i) for i in k.values() ])
        
        i = list(k.values())
        j = list(k.keys())         
        print(s)
        
    return j[i.index(max(i))]