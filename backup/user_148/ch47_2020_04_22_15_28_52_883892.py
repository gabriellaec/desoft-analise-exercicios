def estritamente_crescente(l):
    l2 = []
    i = 0
    
    while i<len(l):
        if len(l)==0:
            return l2
        if len(l)>0:
            if l[i+1]>l[i]:
                l2[0] = l[0]
                l2.append(l[i+1])
                i += 1
     
    return l2
            