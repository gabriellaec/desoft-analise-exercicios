def soma_impares(x):
    a=[0]
    for i in range (len(x)):
        if not x[i]%2==0:
            a.append(x[i])
    y = sum(a)
    return y