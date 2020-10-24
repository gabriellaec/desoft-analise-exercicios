def estritamente_crescente(l):
    l2 = []
    l2[0] = l[0]
    i = 1
    
    while i<len(l):
        if l[i] > l[i-1]:
            l2.append(l[i])
        i += 1
        
    return l2 
