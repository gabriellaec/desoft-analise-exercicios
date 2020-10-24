def conta_a(s):
    l2 = []
    i = 0
    
    while i<len(s):
        if s[i] == 'a':
            l2.append(s[i])
        i += 1
        
    return len(l2)