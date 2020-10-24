def soma_impares(l):
    s=0
    for i in range(len(l)):
        if l[i]%2!=0:
            s+=l[i]
    return s
            
            