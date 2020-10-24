def estritamente_crescente(l):
    l2 = []
    l[0] = l2[0]
    i = 0
    
    while i<len(l):
        if l[i+1] > l[i]:
            l2.append(l[i+1])
        i += 1
        
    return l2
