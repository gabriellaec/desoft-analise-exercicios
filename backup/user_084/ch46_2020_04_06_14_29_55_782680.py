def numero_no_indice(l):
    s=[]
    for i in range(len(l)):
        if i==l[i]:
            s.append(i)    
    return s
        
    