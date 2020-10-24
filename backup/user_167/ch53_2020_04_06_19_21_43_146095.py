def soma_impares (l):
    i=0
    s=0
    while i <= len(l):
        if l[i] % 2 == 0:
            i+=1
        else:
            s+=l[i]
            
    