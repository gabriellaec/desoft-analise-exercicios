def soma_impares(x):
    a=[]
    i=0
    while i<len(x):
        if x[i]%2!=0:
            a.append(x[i])
    y = sum(a)
    return y