def inverte_lista(list):
    n=len(list)
    if n == 0:
        return []
    new = []*n
    i=0
    
    while i < n:
        new[n-i]=list[i]
        i=i+1
        
    return new