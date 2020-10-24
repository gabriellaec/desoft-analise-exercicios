def soma_impares(n):
    i=0
    ne=0
    while i<len(n):
        if n[i]%2!=0:
            ne+=n[i]
        i+=1
    return ne
           