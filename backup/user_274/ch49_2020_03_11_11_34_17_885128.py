def inverte_lista(list):
    n=len(list)
    new = []*n
    i=0
    
    while i < n:
        new[n-i]=list[i]
        i=i+1
        
    return new