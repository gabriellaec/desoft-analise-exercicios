def soma_impares(x, a):
    i=0
    while i<len(x):
        if not x[i]%2==0:
            a.append(x[i])
        i+=1
    y = sum(a)
    return y