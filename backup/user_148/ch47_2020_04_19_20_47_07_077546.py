def estritamente_crescente(l):
    l2 = []
    i = 0
    
    while i<len(l):
        l2[0] = l[0]
        if l[i+1] > l[i]:
            l2.append(l[i+1])
        i += 1
        
    return l2 
