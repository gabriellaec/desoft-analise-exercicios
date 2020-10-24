def inverte_lista(list):
    n=len(list)
    if n == 0:
        return []
    new = []
    i=0
    m=n-1
    
    while i < n:
        a=list[m-i]
        new.append(a)
        i=i+1
        
    return new