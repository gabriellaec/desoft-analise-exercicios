def estritamente_crescente(list):
    n=len(list)
    if n == 0:
        new = []
        return new
    r=list[0]
    i=1
    new=[list[0]]
    
    while i < n:
        if list[i] > r:
            new.append(list[i])
            r=list[i]
        i=i+1
    
    return new
        