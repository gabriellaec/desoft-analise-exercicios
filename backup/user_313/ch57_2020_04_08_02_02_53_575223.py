def verifica_progressao (l1):
    a = [0]*(len(l1)-1)
    b = [0]*(len(l1)-1)
    cont = 0
    for i in l1:
        if i == 0:
            cont+=1
        if cont >= len(l1):
            return 'NA'
    for i in range(0,len(l1)-1):
        a[i] = l1[i+1]-l1[i]
        b[i] = l1[i+1]/l1[i]
    

    
    if a[len(a)-1] == a[0] and b[len(b)-1] == b [0]:
        return 'AG'
        
    elif a[len(a)-1] == a[0]:
        return 'PA'
    
    elif b[len(b)-1] == b [0]:
        return 'PG'
    
    else:
        return 'NA'