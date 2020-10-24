def eh_crescente(l):
    i=1
    a=True
    
    while i<len(l):
        if l[i]>l[i-1]:
            a=True
        else:
            return False
        i+=1