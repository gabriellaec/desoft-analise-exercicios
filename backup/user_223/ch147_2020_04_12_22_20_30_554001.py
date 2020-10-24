def mais_frequente(l1):
    dic={}
    for e in l1:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
    oc = 0       
    for n in dic.values():        
        if n>oc:
            oc == n
            
    for p,o in dic.items():
        if o == oc:
            return p