def verifica_progressao (l1):
    a = [0]*(len(l1)-1)
    b = [0]*(len(l1)-1)
    for i in range(0,len(l1)-1):
        a[i] = l1[i+1]-l1[i]
        b[i] = l1[i+1]/l1[i]
    
    X = len(a)
    y = len(b)
    
    if a[len(a)-1] == a[0] and b[len(b)-1] == b [0]:
        return 'AG'
        
    elif a[len(a)-1] == a[0]:
        return 'PA'
    
    elif b[len(b)-1] == b [0]:
        return 'PG'
    
    else:
        return 'NA'