def eh_crescente(l):
    i=1
    a=True
    
    while l[i]>l[i-1]:
        a=True
        i+=1
    return a