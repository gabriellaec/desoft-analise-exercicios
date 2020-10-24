n=100001010101
def quantos_uns(n):
    y=str(n)
    c=0
    q=0
    while c<len(y):
        if y[c]==1:
            q+=1
            c+=1  
        else:
            c+=1
    return q